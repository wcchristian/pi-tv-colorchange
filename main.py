from colorthief import ColorThief
from phue import Bridge
from rgbxy import Converter
from rgbxy import GamutC
from colorchanger import colorchanger
import cv2
import os
import time

converter = Converter(GamutC)
b = Bridge('192.168.1.3')
# b.connect()

def images():
    for i in range(0, 58):
        start = time.time()
        print('Starting pass', i)

        colorchanger.change_color('video/frame'+str(i)+'.jpg', b, converter)
        time.sleep(1)

        end = time.time()
        print('This pass took', end - start)

def video():
        # Path to video file 
    vidObj = cv2.VideoCapture('images/video.mov') 
  
    # Used as counter variable 
    count = 0
    imgCount = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 

        success, image = vidObj.read() 
        if count % 100 == 0:
            cv2.imwrite("video/frame%d.jpg" % imgCount, image) 
            imgCount += 1
  
        count += 1

def capture_image_over_time():
    # initialize the camera
    while True:
        # time.sleep(1)
        cam = cv2.VideoCapture(0)
        ret, image = cam.read()

        if ret:
            cv2.imwrite('fooo2.jpg',image)
        cam.release()

        start = time.time()

        colorchanger.change_color('fooo2.jpg', b, converter)

        os.remove("fooo2.jpg")
        os.rem
        end = time.time()
        print('This pass took', end - start)

capture_image_over_time()