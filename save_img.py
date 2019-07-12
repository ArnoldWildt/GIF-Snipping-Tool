import imageio
from threading import Thread


def thread_save_img(path, image):
    imageio.imwrite(path, image, quality=40)


def save_img(path, image):
    x = Thread(target=thread_save_img,
               args=(path, image))
    x.start()


def save_png_disk(path, image):
    imageio.imwrite(path, image)
