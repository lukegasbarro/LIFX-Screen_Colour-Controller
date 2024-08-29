from PIL import ImageGrab
import numpy as np


def get_top_third_rgb():

    screenshot = ImageGrab.grab()
    width, height = screenshot.size
    top_third_region = (0, 0, width, height // 3)
    top_third_image = screenshot.crop(top_third_region)

    rgb_image = top_third_image.convert('RGB')

    # Compute the average RGB value of the top third
    pixel_data = np.array(rgb_image)
    avg_rgb = np.mean(pixel_data, axis=(0, 1)).astype(int)

    return tuple(avg_rgb)


def get_rgb():

    avg_rgb = get_top_third_rgb()
    R, G, B = avg_rgb
    print(f"Average Top Third Screen RGB: {avg_rgb}")

    return R, G, B


get_rgb()
