# Daniel Severa, Jr., TWK 2023
# a part of the Diffusionbooth/Partyclick project
# https://github.com/orlop/partyclick.git

# snapshot.py takes care of the camera logic

# picamera2 is the new libcamera based python library.
# Required for the proper functionality of Raspberry Pi Camera Module v3
from picamera2 import Picamera2
import time

# snap() takes a picture and saves it to a shared SMB location
def snap():
    picam2 = Picamera2()

    picam2.start_and_capture_file(name="/home/partyclick/shared/image.jpg", delay=0, captire_mode="still", showPreview=False)