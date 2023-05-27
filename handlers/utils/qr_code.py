from pyzbar.pyzbar import decode
from PIL import Image
from pyzbar import pyzbar
import qrcode
import cv2
from glob import glob
import os.path

# path = '.'
# num_files = len([f for f in os.listdir(path)
#                  if os.path.isfile(os.path.join(path, f))])


def create_qr(data):
    path = os.getcwd() + '\\handlers\\utils\\qr_code'
    num_files = len([f for f in os.listdir(path)
                     if os.path.isfile(os.path.join(path, f))])

    qr = qrcode.QRCode()
    qr.add_data(str(data))
    img = qr.make_image()
    img.save(f'{path}/dog_qr_{num_files}.jpg')
    return (f'{path}/dog_qr_{num_files}.jpg')


def read_qr(path):
    img = Image.open(path)
    result = decode(img)
    for i in result:
        return (i.data.decode("utf-8"))