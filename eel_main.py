import eel
import base64
from capture import Capture
from PIL import Image
from io import BytesIO
from save_img import save_img
import time
import os

eel.init('web')

capture_instance = Capture()

if not os.path.isdir("./img/"):
    os.mkdir("./img/")


def convert_image(img):
    buffered = BytesIO()

    img = Image.fromarray(img)
    img = img.convert("RGB")
    img.save(buffered, format="JPEG")

    img_base64 = base64.b64encode(buffered.getvalue())
    return str(img_base64)


def send_image(img_base64):
    eel.set_image(img_base64)


@eel.expose
def stop_record():
    eel.show_wait_modal()
    if capture_instance.stop_recording():
        eel.show_ok_modal()


@eel.expose
def start_record():
    print("Eel_main start record")
    capture_instance.start_recording()


@eel.expose
def save_png(mode):
    if mode == "window":
        eel.set_modal_eel("show")

    img = capture_instance.capture_mode(mode)
    save_img(f"{int(time.time())}.png", img[..., ::-1])

    eel.set_modal_eel("hide")


@eel.expose
def get_preview(mode):
    if mode == "window":
        eel.set_modal_eel("show")

    img = capture_instance.capture_mode(mode)
    send_image(convert_image(img))

    eel.set_modal_eel("hide")


eel.start('main.html', size=(1400, 800))
