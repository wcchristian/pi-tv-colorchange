from colorchanger import colorchanger
import cv2
import time
import config


def capture_image_over_time():
    while True:
        time.sleep(config.sample_time)
        cam = cv2.VideoCapture(0)
        ret, image = cam.read()

        if ret:
            start = time.time()
            colorchanger.change_color_based_on_image(image)
            end = time.time()
            if config.debug_logging:
                print('This pass took', end - start)
        else:
            if config.debug_logging:
                print('Image failed to capture...')

        cam.release()


capture_image_over_time()
