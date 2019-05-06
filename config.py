# Usage
mode = 1

# Calibration
# Main Configuration
bridge_ip_address = '192.168.1.3'      # The IP Address of your hue bridge on your network
sample_time = 0                        # How Often to take a new image sample
image_color_detect_quality_gate = 100  # Quality gate for the dominant color algorithm
image_sample_percent = 0.5             # how much to scale the image down in percent before sampling. Helpful for aiming
image_sample_padding = (0, 0)          # x, y padding for image sample box
tmp_image_name = 'tmp.jpg'

# Resize
resize_image = False                   # Could improve processing time between colors.
resize_height = 100                    # The height to resize
resize_width = 100                     # the Width to resize

# Hue
hue_light_id = 9                       # The Id of the hue light in regards to the bridge.

# Debug
debug_window_name = 'Image Debug'      # The name of the debug window to show the image sample.
debug_box_color = (0, 255, 0)          # The color of the box to draw on the image in the debug window.
debug_box_size = 2                     # The thickness of the line to show in the debug window
debug = False                          # If debug mode is on or not.
debug_gui = True
debug_logging = True                   # If the program should log
debug_static_img_name = 'calibrate.jpg'

# Blynk
blynk_on = False
blynk_key = ''
