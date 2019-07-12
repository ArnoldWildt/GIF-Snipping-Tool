import ctypes
import ctypes.wintypes
#import d3dshot
from region_grab import RegionGrab
from win32gui import (
    GetWindowText,
    GetForegroundWindow,
    FindWindow,
    GetWindowRect,
    ShowWindow,
    SetForegroundWindow,
)

# Debugging
import sys

SW_MINIMIZE = 6
SW_RESTORE = 9


class Capture():
    def __init__(self):
        self.mode_type = None
        self.capture_type = None
        self.select_dict = {
            "screen": self.screen_capture,
            "window": self.window_capture,
            "region": self.region_capture,
            "full": self.full_capture,
        }
        self.capture_instance = None

    def start_recording(self):
        gif_app = GetForegroundWindow()
        ShowWindow(gif_app, SW_MINIMIZE)
        self.capture_instance.start_capture()

    def stop_recording(self):
        return self.capture_instance.stop_capture()

    def capture_mode(self, mode_type):
        self.capture_type = mode_type
        img = self.select_dict[self.capture_type]()
        return img

    def screen_capture(self):
        # TODO: Select which Screen
        # d3d_window = d3dshot.create(capture_output="numpy")
        # return d3d_window.screenshot()
        pass

    def window_capture(self):
        self.capture_instance = RegionGrab()
        return self.capture_instance.preview_window()

    def region_capture(self):
        gif_app = GetForegroundWindow()
        ShowWindow(gif_app, SW_MINIMIZE)

        self.capture_instance = RegionGrab()
        prev_img = self.capture_instance.preview_region()
        ShowWindow(gif_app, SW_RESTORE)
        set_foreground(gif_app)

        return prev_img

    def full_capture(self):
        self.capture_instance = RegionGrab()
        return self.capture_instance.preview_full()


def get_foreground():
    return GetWindowText(GetForegroundWindow())


def set_foreground(hwnd):
    try:
        SetForegroundWindow(hwnd)
    except:
        print(f"Can't set Window to Foreground")
        print("Unexpected error:", sys.exc_info())
