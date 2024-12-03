import time
import logging
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooser
from androidhelper import Android  # Requires SL4A for Android
import cv2
import numpy as np

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    handlers=[logging.StreamHandler()]
)

# Android-specific helper
droid = Android()

# Configuration file location
CONFIG_FILE = "/sdcard/mad_smash_config.txt"

# Adaptive scaling based on device resolution
def get_scaling_factor():
    try:
        result = os.popen("wm size").read()
        native_resolution = [int(i) for i in result.split()[-1].split("x")]
        reference_resolution = [1080, 1920]  # Reference resolution for coordinates
        scale_x = native_resolution[0] / reference_resolution[0]
        scale_y = native_resolution[1] / reference_resolution[1]
        return scale_x, scale_y
    except Exception as e:
        logging.error(f"Error retrieving screen resolution: {e}")
        return 1.0, 1.0

SCALE_X, SCALE_Y = get_scaling_factor()

def scale_coordinates(coords):
    """Scale coordinates based on the device's screen resolution."""
    if coords:
        return int(coords[0] * SCALE_X), int(coords[1] * SCALE_Y)
    return None

# Function to simulate taps
def tap(x, y):
    x, y = scale_coordinates((x, y))
    os.system(f"input tap {x} {y}")
    droid.makeToast(f"Tapped at ({x}, {y})")

# Function to detect images on screen using OpenCV
def is_image_on_screen(image_path, threshold=0.8):
    try:
        screenshot_path = "/sdcard/screen.png"
        os.system(f"screencap -p {screenshot_path}")

        screen_img = cv2.imread(screenshot_path)
        template = cv2.imread(image_path, 0)
        screen_gray = cv2.cvtColor(screen_img, cv2.COLOR_BGR2GRAY)

        result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)

        return max_val >= threshold
    except Exception as e:
        logging.error(f"Error detecting image: {e}")
        return False

# GUI for game automation setup
class GameAutomationGUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.play_coords = None
        self.move_coords = None
        self.play_again_coords = None
        self.images = {}

        self.add_widget(Label(text="Mad Smash Automation", font_size=24))
        self.add_widget(Button(text="Set 'Play' Button Location", on_press=self.set_play_coords))
        self.add_widget(Button(text="Set 'Move' Location", on_press=self.set_move_coords))
        self.add_widget(Button(text="Set 'Play Again' Button Location", on_press=self.set_play_again_coords))
        self.add_widget(Button(text="Upload 'Won' Indicator Image", on_press=lambda x: self.upload_image('won')))
        self.add_widget(Button(text="Upload 'Lost' Indicator Image", on_press=lambda x: self.upload_image('lost')))
        self.add_widget(Button(text="Save Configuration", on_press=self.save_configuration))
        self.add_widget(Button(text="Load Configuration", on_press=self.load_configuration))
        self.add_widget(Button(text="Start Automation", on_press=self.start_automation))

        self.status_label = Label(text="Status: Waiting for setup...")
        self.add_widget(self.status_label)

    def set_play_coords(self, instance):
        droid.makeToast("Tap on 'Play' button in the game, then return here.")
        Clock.schedule_once(lambda dt: self.record_coordinates('play'), 2)

    def set_move_coords(self, instance):
        droid.makeToast("Tap on the screen's move area, then return here.")
        Clock.schedule_once(lambda dt: self.record_coordinates('move'), 2)

    def set_play_again_coords(self, instance):
        droid.makeToast("Tap on the 'Play Again' button, then return here.")
        Clock.schedule_once(lambda dt: self.record_coordinates('play_again'), 2)

    def record_coordinates(self, key):
        coords = droid.getLastKnownLocation()
        if coords:
            lat, lon = coords.get("gps", {}).get("latitude", 0), coords.get("gps", {}).get("longitude", 0)
            self.status_label.text = f"Coordinates recorded for {key}: ({lat}, {lon})"
            setattr(self, f"{key}_coords", (lat, lon))
        else:
            self.status_label.text = f"Failed to record {key} coordinates. Try again."

    def upload_image(self, key):
        file_chooser = FileChooser()
        popup = Popup(title=f"Select {key.capitalize()} Image", content=file_chooser, size_hint=(0.9, 0.9))
        popup.open()

        def on_selection(instance, selection):
            if selection:
                self.images[key] = selection[0]
                self.status_label.text = f"Uploaded {key} image: {selection[0]}"
                popup.dismiss()

        file_chooser.bind(on_selection=on_selection)

    def save_configuration(self, instance):
        try:
            with open(CONFIG_FILE, "w") as f:
                f.write(f"play_coords={self.play_coords}\n")
                f.write(f"move_coords={self.move_coords}\n")
                f.write(f"play_again_coords={self.play_again_coords}\n")
                f.write(f"images={self.images}\n")
            self.status_label.text = "Configuration saved successfully!"
        except Exception as e:
            self.status_label.text = f"Error saving configuration: {e}"

    def load_configuration(self, instance):
        try:
            with open(CONFIG_FILE, "r") as f:
                config = eval(f.read())
                self.play_coords = config.get("play_coords")
                self.move_coords = config.get("move_coords")
                self.play_again_coords = config.get("play_again_coords")
                self.images = config.get("images")
            self.status_label.text = "Configuration loaded successfully!"
        except Exception as e:
            self.status_label.text = f"Error loading configuration: {e}"

    def start_automation(self, instance):
        if not all([self.play_coords, self.move_coords, self.play_again_coords, self.images]):
            self.status_label.text = "Please complete setup before starting."
            droid.makeToast("Setup incomplete!")
        else:
            self.status_label.text = "Starting automation..."
            droid.makeToast("Starting Mad Smash automation!")
            self.play_games()

    def play_games(self):
        for game_num in range(1, 6):  # Adjust as needed
            self.status_label.text = f"Playing game {game_num}..."
            tap(*self.play_coords)  # Tap Play button
            time.sleep(3)  # Wait for the game to start
            self.play_game_loop()

            # Tap Play Again after each game
            tap(*self.play_again_coords)
            time.sleep(1)

    def play_game_loop(self):
        for _ in range(20):  # Simulate 20 taps per game
            tap(*self.move_coords)
            time.sleep(0.2)  # Adjust timing for game speed

            # Check for game win/loss
            if is_image_on_screen(self.images.get('won')):
                self.status_label.text = "Game won!"
                break
            elif is_image_on_screen(self.images.get('lost')):
                self.status_label.text = "Game lost!"
                break

# App entry point
class MadSmashApp(App):
    def build(self):
        return GameAutomationGUI()

if __name__ == "__main__":
    try:
        MadSmashApp().run()
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        droid.makeToast("Mad Smash Automation crashed. Check logs for details.")
