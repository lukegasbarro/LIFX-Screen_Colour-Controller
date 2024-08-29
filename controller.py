# This script is used to control a single LIFX bulb. It captures screen contents
# and sets the color of the LIFX bulb to the average colour displayed on the screen.
# By Luke Gasbarro.

# Note: Press Ctrl+C to exit the program when running in the terminal.

import requests
import time
import screenCaptureTopThird
import screenCapture

# LIFX API token - Obain from https://cloud.lifx.com/settings
token = "YOUR_LIFX_API"

headers = {
    "Authorization": "Bearer %s" % token,
}

# LED Settings - Adjust to suit your preference.

BRIGHTNESS = 0.25
DURATION = 2        # Duration of the transition in seconds. Works best with 2 seconds where a request is made every 2 seconds.

if __name__ == '__main__':
    try:
        while True:
            # Wait 2 seconds - This limits the rate of requests to the LIFX API. 
            # Max 1 request per second as per LIFX documentation.
            time.sleep(2)

            # Comment out the line below and uncomment the line below that to switch between capturing the entire screen and capturing 
            # the top third of the screen for the average colour calculation. Best results will vary depending on the application.

            # R, G, B = screenCapture.get_rgb()
            R, G, B = screenCaptureTopThird.get_rgb()

            payload = {
                "power": "on",
                "color": "rgb:"+str(R)+","+str(G)+","+str(B),
                "brightness": BRIGHTNESS,
                "duration": DURATION
            }

            response = requests.put(
                'https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
    except KeyboardInterrupt:
        print("Program exited by user.")

