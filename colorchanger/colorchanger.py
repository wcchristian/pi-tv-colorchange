from colorthief import ColorThief
import cv2
import config
from phue import Bridge
from rgbxy import Converter
from rgbxy import GamutC
import os

converter = Converter(GamutC)
hue_bridge = Bridge(config.bridge_ip_address)


def change_color_based_on_image(img):

    if config.resize_image:
        img = cv2.resize(img, (config.resize_width, config.resize_height))

    h, w, c = img.shape
    min_x, min_y, max_x, max_y = get_sample_zone_coordinates(h, w)

    if config.debug:
        draw_debug_image(img, (min_x, min_y), (max_x, max_y))

    sample_img = img[min_y:max_y, min_x:max_x]
    cv2.imwrite('tmp.jpg', sample_img)
    dominant_color = find_dominant_color('tmp.jpg')
    os.remove('tmp.jpg')
    set_hue_color(config.hue_light_id, dominant_color)


def draw_debug_image(image, rect_start, rect_end):
    img2 = cv2.rectangle(image, rect_start, rect_end, config.debug_box_color, config.debug_box_size)
    cv2.imshow(config.debug_window_name, img2)
    cv2.waitKey(1)


def get_sample_zone_coordinates(h, w):
    tp_height = h*config.image_sample_percent
    tp_width = w*config.image_sample_percent

    min_y = int((h - tp_height) / 2)
    min_x = int((w - tp_width) / 2)

    max_y = int(min_y + tp_height)
    max_x = int(min_x + tp_width)

    min_x += config.image_sample_padding[0]
    max_x += config.image_sample_padding[0]

    min_y += config.image_sample_padding[1]
    max_y += config.image_sample_padding[1]

    return min_x, min_y, max_x, max_y


def find_dominant_color(file_name):
    color_thief = ColorThief(file_name)
    dominant_color = color_thief.get_color(quality=config.image_color_detect_quality_gate)
    return dominant_color


def set_hue_color(hue_light_id, rgb_color):
    xy = converter.rgb_to_xy(rgb_color[0], rgb_color[1], rgb_color[2])
    if config.debug_logging:
        print('Setting light to color', rgb_color)
    hue_bridge.set_light(hue_light_id, 'xy', xy)
