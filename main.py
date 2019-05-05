from phue import Bridge
from rgbxy import Converter
from rgbxy import GamutC
from colorchanger import colorchanger
import cv2
import os
import time
import config

converter = Converter(GamutC)
b = Bridge(config.bridge_ip_address)
# b.connect()


def capture_image_over_time():
    # initialize the camera
    while True:
        time.sleep(config.sample_time)
        cam = cv2.VideoCapture(0)
        ret, image = cam.read()
        cv2.imshow(config.debug_window_name, image)
        cv2.waitKey(1)

        if ret:
            cv2.imwrite(config.tmp_file_name, image)
        cam.release()

        start = time.time()

        colorchanger.change_color(config.tmp_file_name, b, converter)
        # TODO: Change this to take the image and not have to read/write?

        os.remove(config.tmp_file_name)
        end = time.time()
        print('This pass took', end - start)


capture_image_over_time()
