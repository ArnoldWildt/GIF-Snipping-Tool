import win32gui
import win32ui
from win32con import SRCCOPY
import numpy as np
import d3dshot

d = d3dshot.create(capture_output="numpy")


def grab_screen(region):
    '''
    Input Region | Output np array\n
    Region = width, height, left, top
    '''
    width, height, left, top = region

    d.screenshot(region=())

    return img
