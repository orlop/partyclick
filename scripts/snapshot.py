# Daniel Severa, Jr., TWK 2023
# a part of the Diffusionbooth/Partyclick project
# https://github.com/orlop/partyclick.git

# picamera2 is the new libcamera based python library.
# Required for the proper functionality of Raspberry Pi Camera Module v3
from picamera2 import Picamera2, Preview 
import time

picam2 = Picamera2()
picam2.capture_file("/home/partyclick/test.jpg")