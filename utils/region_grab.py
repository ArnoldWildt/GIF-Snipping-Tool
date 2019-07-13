import ctypes
import ctypes.wintypes
import numpy as np
from .screen_resolution import get_screen_res
from .region_selector import RegionSelector
from .screen_grab import grab_screen
from .save_img import save_img
from threading import Thread
from PyQt5 import QtWidgets
from time import time
from win32gui import (
    GetWindowText,
    GetForegroundWindow,
    FindWindow,
    GetWindowRect,
    ShowWindow,
    SetForegroundWindow,
)

import sys
# Testing
import imageio
import os


def full_nums(num):
    return (5 - len(str(num))) * '0' + str(num)


class RegionGrab():
    def __init__(self):
        self.running = True
        self.region = None
        self.frames = []

        # Saving Counter
        self.img_nums = 0

    def get_img(self):
        img = grab_screen(self.region)

        # Remove Alpha channel from Image
        img = img[..., :-1]

        img = img[..., ::-1]

        return img

    def preview_full(self):
        self.region = get_screen_res()
        return self.get_img()

    def preview_region(self):
        app = QtWidgets.QApplication([''])
        window = RegionSelector()
        window.show()
        app.exec_()

        self.region = window.get_region()
        print(self.region)

        return self.get_img()

    def preview_window(self):
        current_win = get_foreground()

        while current_win == get_foreground() or len(get_foreground()) <= 0:
            pass

        capture_win = get_foreground()

        hwndMain = FindWindow(None, capture_win)

        # Function to get the RECT of window handle
        DwmGetWindowAttribute = ctypes.windll.dwmapi.DwmGetWindowAttribute
        DWMWA_EXTENDED_FRAME_BOUNDS = 9

        rect = ctypes.wintypes.RECT()
        DwmGetWindowAttribute(hwndMain,
                              ctypes.wintypes.DWORD(
                                  DWMWA_EXTENDED_FRAME_BOUNDS),
                              ctypes.byref(rect),
                              ctypes.sizeof(rect)
                              )

        print(rect.left, rect.top, rect.right, rect.bottom)
        width = abs(rect.right - rect.left)
        height = abs(rect.bottom - rect.top)

        window_pos = [width, height, rect.left, rect.top]

        hwnd_app = FindWindow(None, "GIF Snipping Tool")

        # Doesn't work on Windows Apps?
        set_foreground(hwnd_app)

        self.region = window_pos

        return self.get_img()

    def capture_region(self):
        self.running = True

        while self.running:
            self.img_nums += 1
            img = self.get_img()

            save_img(f"./img/{full_nums(self.img_nums)}.jpeg", img)

        self.img_nums = 0

    def stop_capture(self):
        self.running = False

        with imageio.get_writer(f'{int(time())}.gif',
                                mode='I',
                                fps=60,
                                subrectangles=True) as writer:

            for jpeg_file in os.listdir(f"./img/"):
                image = imageio.imread(f"./img/{jpeg_file}")
                writer.append_data(image)
                os.remove(f"./img/{jpeg_file}")

            # Final cleanup
            for jpeg_file in os.listdir(f"./img/"):
                os.remove(f"./img/{jpeg_file}")

        print("saved file")
        return True

    def start_capture(self):
        capture_thread = Thread(target=self.capture_region)
        capture_thread.start()
        print("thread record")


def get_foreground():
    return GetWindowText(GetForegroundWindow())


def set_foreground(hwnd):
    try:
        SetForegroundWindow(hwnd)
    except:
        print(f"Can't set Window to Foreground")
        print("Unexpected error:", sys.exc_info())


if __name__ == "__main__":
    pass
