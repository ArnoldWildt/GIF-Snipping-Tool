import cv2
from threading import Thread


def thread_save_img(path, image):
    cv2.imwrite(path, image, params=[int(cv2.IMWRITE_JPEG_QUALITY), 40])


def save_img(path, image):
    x = Thread(target=thread_save_img,
               args=(path, image))
    x.start()


def save_png(path, image):
    cv2.imwrite(path, image)
