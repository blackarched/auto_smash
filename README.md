Auto_Smash Automation Tool

The Mad Smash Automation Tool is a Python-based automation script designed to enhance your gameplay experience in the popular Android game Mad Smash. Whether you're looking to save time or optimize your performance, this tool brings cutting-edge automation features to your fingertips.

This tool provides a user-friendly GUI, dynamic resolution adaptation, and state-of-the-art image recognition to handle gameplay autonomously. It is optimized for real-world use on Android devices, offering a seamless setup, robust performance, and the ability to adapt to different screen resolutions and device configurations.

Why Use Mad Smash Automation Tool?
Mad Smash is an engaging game, but repetitive actions like tapping and restarting can be tedious. This tool automates these tasks for you, letting you focus on enjoying the results while ensuring precision and efficiency. The adaptive features ensure it works flawlessly across various devices, making it versatile and future-ready.

Features
Core Features
Adaptive Resolution Handling:

Dynamically adjusts coordinates and scaling to match the screen resolution of your Android device.
Ensures precise taps regardless of device size or DPI settings.
Advanced Image Recognition:

Detects game states (Win/Loss) using OpenCV-based template matching.
Supports custom thresholds for detection accuracy.
Dynamic Configuration:

Easily set and update button locations (Play, Move, Play Again).
Upload custom images for game state indicators (Win/Loss).
Save and Load Configurations:

Save your setup for future sessions to avoid repetitive configurations.
Load saved configurations in just one click.
Cross-Device Compatibility:

Works on Android devices with diverse screen sizes and resolutions.
Optimized for devices running Pydroid 3 or similar Python environments.
Real-Time Feedback:

Displays clear status messages during operation.
Provides real-time updates via Toast notifications on your Android device.
Efficient Gameplay Automation:

Automates repetitive tasks like tapping to move or restarting the game.
Ensures error-free execution with comprehensive error handling.
User-Friendly GUI:

Intuitive interface built with Kivy for easy navigation and setup.
Step-by-step guidance to complete the configuration process.
Technical Features
Touch Simulation:

Uses Android's input tap command to simulate accurate screen touches.
Comprehensive Logging:

Logs all actions, errors, and detections for easier debugging and tracking.
Adaptive Learning:

The tool learns from user-configured settings, improving precision and usability over time.
Error Handling:

Graceful handling of missing configurations or invalid inputs.
Prevents crashes and ensures smooth operation.
Installation
System Requirements
Android Device: Compatible with most Android smartphones and tablets.
Python Environment: Install Pydroid 3.
Free Storage Space: At least 100 MB for dependencies and configurations.
Steps to Install
Install Pydroid 3:

Download and install Pydroid 3 from the Google Play Store.
Install Required Libraries:

Open Pydroid 3 and create a new Python script.
Open the terminal in Pydroid 3 and run:
bash
Copy code
pip install -r requirements.txt
Download the Script:

Save the mad_smash_automation.py script to a known location on your Android device (e.g., /sdcard/).
Run the Script:

Open the script in Pydroid 3 and press Run to launch the GUI.
Usage
Setting Up the Tool
Launch the Script:

Run mad_smash_automation.py in Pydroid 3.
The GUI will open, guiding you through the setup process.
Set Button Locations:

Use the GUI to set coordinates for:
Play Button: To start a new game.
Move Area: Where the tool will simulate taps during gameplay.
Play Again Button: To restart the game after completion.
Upload Game State Images:

Upload screenshots of the game’s Win and Loss indicators for precise detection.
Save Your Configuration:

Save your setup for future sessions to avoid repeating these steps.
Start Automation:

Once all configurations are complete, click Start Automation.
The tool will take over gameplay, automating taps and restarts based on game states.
Troubleshooting
Common Issues and Fixes
Dependencies Not Installed:

Error: "Module not found" when running the script.
Fix: Install all required libraries using:
bash
Copy code
pip install -r requirements.txt
Misaligned Taps:

Issue: The tool taps in incorrect locations.
Fix:
Reconfigure button locations in the GUI.
Ensure the screen resolution scaling is accurate.
Image Detection Fails:

Issue: The tool cannot detect Win/Loss states.
Fix:
Ensure the uploaded images match the game’s UI exactly.
Adjust the threshold value in the is_image_on_screen function for stricter or lenient detection.
Script Crashes:

Issue: Unexpected script termination.
Fix:
Check logs for errors.
Ensure Pydroid 3 has necessary permissions (e.g., storage access).
Advanced Usage
Customizing Detection Accuracy
Modify the threshold parameter in the is_image_on_screen function to control the sensitivity of image recognition.
Testing with Multiple Resolutions
If using devices with different resolutions, reconfigure the scaling factor in the get_scaling_factor() function for optimized performance.
Contributing
Contributions are welcome! If you have ideas for improvements or bug fixes, feel free to fork this repository and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Special thanks to:

The developers of Pydroid 3 for enabling Python development on Android.
OpenCV and Kivy communities for their robust libraries and documentation.
requirements.txt
plaintext
Copy code
kivy==2.1.0
opencv-python==4.5.5.62
numpy==1.21.6
androidhelper==0.1.0
This README.md provides all necessary details for installing, configuring, and troubleshooting the tool.









