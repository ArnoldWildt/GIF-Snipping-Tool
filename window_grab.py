import cv2
import numpy as np
from screen_grab import grab_screen
from save_img import save_img
from PIL import Image


class WindowGrab():
        def __init__(self):
                self.running = True
                self.region = None
                self.frames = []


def swap_index(i):
        return [i[2], i[3], i[0], i[1]]


def window_grab(preview=False, region=None):

    # region = swap_index(region)

    # frames = []

    if preview:
        img = grab_screen(region)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img

if __name__ == "__main__":
    window_grab()
