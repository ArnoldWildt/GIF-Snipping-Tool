from io import BytesIO
import base64
import imageio


def convert_image(img):
    buffered = BytesIO()

    imageio.imwrite(buffered, img, format="JPEG")

    img_base64 = base64.b64encode(buffered.getvalue())
    return str(img_base64)
