from PIL import ImageGrab
import numpy as np


def get_screen_rgb():

    screenshot = ImageGrab.grab()
    rgb_image = screenshot.convert('RGB')

    # Compute the average RGB value of the screenshot
    pixel_data = np.array(rgb_image)
    avg_rgb = np.mean(pixel_data, axis=(0, 1)).astype(int)

    return tuple(avg_rgb)


def get_rgb():

    avg_rgb = get_screen_rgb()
    R, G, B = avg_rgb
    #print(f"Average Screen RGB: {avg_rgb}")

    return R, G, B

