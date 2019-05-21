# Raspberry Pi / Hue Lightstrip Camera Color Changer
Description

## Usage
This program was written to be run on a raspberry pi however I did debug it on a macbook pro using the webcam and
that seemed to work fine as well

## Setup
### Hardware Setup
1. It may be wise to give your hue bridge a static ip on your network


### Setting up Raspbian SD Card
1. Download and install raspbian to an sd card using etcher or some other tool.
1. Mount the sd on your computer. In the root create a file named `ssh`
1. Create another file in the root of the card named `wpa_supplicant.conf` and add the following snippet. Change your ssid to your
network name and psk to the password for your network.
```conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid=""
    psk=""
    key_mgmt=WPA-PSK
}
```
1. Put the sd card in the pi and plug it in so it boots.

### Pi Setup
1. ssh into the pi with `ssh pi@raspberrypi.local` the default password is `raspberry`
1. run `sudo raspi-config`
1. Enable VNC, change the password, and change the hostname of the pi
1. Exit ssh

### VNC Work
1. Log into the pi via [VNC](https://www.realvnc.com/en/connect/download/viewer)
1. Take a sample image via command line using `raspistill -o ~/Desktop/test.jpg`
1. Make sure the image appears.
1. Simply copy this repo to the pi using vnc viewer OR cloning the repo on the pi itself.

### Configure The Program
1. In the directory of the program, run `pip3 install -r requirements.txt`
1. Using the info from config description below. Setup config.py for your configuration.
1. Run the program in config mode (Debug = True, Blink_on = False)
1. Make sure that the image lines up with the display you will be sampling
1. Turn (Debug = False, Blink_on = False)
d
### Setup Blynk
1. Download Blynk from the app store
1. Create a new project and copy the key into config.py
1. Add a button and set it up with the virtual pin in your configuration
1. Turn blink_on = True

## Usage
This program was written to be run on a raspberry pi however I did debug it on a macbook pro using the webcam and
that seemed to work fine as well

If you have the raspberry pi gui running run the program in debug mode and adjust / re-run the program config as needed.

If you are not using the raspberry pi gui, set `debug_gui = False` in the config.py file. Then run the program. This should
take an image and then exit. View the image and then continue to run the program and tweak the config as needed until the settings are
to your liking

## Config Description


## Development

## Attribution