from colorchanger import colorchanger
import cv2
import time
import config
import BlynkLib
from threading import Thread

blynk = BlynkLib.Blynk(config.blynk_key)
running = False


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

        if not running:
            break


current_thread = Thread(target=capture_image_over_time)


# Register Virtual Pins
@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):
    global running
    global current_thread

    if current_thread is None:
        current_thread = Thread(target=capture_image_over_time)

    if int(value[0]) == 0:
        print('Turning Off')
        running = False
        current_thread = None
    else:
        print('Turning On')
        running = True
        current_thread.start()


if config.blynk_on:
    print('Starting Blynk Run...')
    while True:
        blynk.run()
else:
    print('Starting program without Blynk...')
    running = True
    capture_image_over_time()
