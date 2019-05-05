from colorthief import ColorThief
import cv2
import os

def change_color(filename, b, converter):
    img = cv2.imread(filename)
    img2 = cv2.resize(img, (1000, 1000))
    h, w, c = img2.shape

    tp_height = h*0.1
    tp_width = w*0.1

    min_h = int((h - tp_height) / 2)
    min_w = int((w - tp_width) / 2)

    max_h = int(min_h + tp_height)
    max_w = int(min_w + tp_width)

    cv2.imwrite('tmpImg.jpeg', img2[min_h:max_h, min_w:max_w])

    color_theif = ColorThief('tmpImg.jpeg')
    dominant_color = color_theif.get_color(quality=100)
    os.remove('tmpImg.jpeg')

    xy = converter.rgb_to_xy(dominant_color[0], dominant_color[1], dominant_color[2])

    print('Setting light to color', dominant_color)
    b.set_light(9, 'xy', xy)