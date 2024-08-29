# LIFX Bulb Screen Colour Control

This repository contains a Python script that controls a LIFX bulb by capturing the screen contents and setting the colour of the bulb to the average colour displayed on the screen. The script can be configured to capture the entire screen or just the top third of the screen for the average colour calculation. 

## Features

- **Screen Colour Synchronization**: The LIFX bulb colour is updated based on the average colour of the screen.
- **Flexible Screen Capture**: Option to capture the entire screen or just the top third.
- **Adjustable LED Settings**: Configure brightness and transition duration to suit your preferences.

## Prerequisites

- A LIFX bulb connected to the internet.
- A LIFX Cloud API token. You can obtain this from the [LIFX Cloud Settings](https://cloud.lifx.com/settings).
- Python 3.9.13
- Required Python libraries: `requests`, `Pillow`, and `numpy`.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/lukegasbarro/LIFX-Screen_Colour-Controller.git
   cd LIFX-Screen_Colour-Controller

2. **Install the required Python libraries**:
    ```bash
    pip install requests Pillow numpy

3. **Set your LIFX API token**:
    Replace YOUR_LIFX_API in the script with your actual LIFX API token in controller.py.

## Usage

1. **Run the script**:
   ```bash
   python controller.py

2. **Switch between screen capture modes**:
    By default, the script captures the top third of the screen.
    To capture the entire screen, uncomment the line with screenCapture.get_rgb() and comment out the line with screenCaptureTopThird.get_rgb().

3. **Stop the script**:
    Press `Ctrl+C` to stop the script.

## Files

- controller.py: Main script to control the LIFX bulb based on screen content.

- screenCapture.py: Contains functions to capture the entire screen and calculate the average RGB values.

- screenCaptureTopThird.py: Contains functions to capture the top third of the screen and calculate the average RGB values.


## Customisation
Note: The following variables can be modified in the controller.py script

- Brightness: Adjust the BRIGHTNESS variable in the script to set the brightness level of the LIFX bulb.

- Transition Duration: Modify the DURATION variable to change the duration of the colour transition.

## Credits

- Luke Gasbarro
