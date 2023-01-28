# Daniel Severa, Jr., TWK 2023
# a part of the Diffusionbooth/Partyclick project
# https://github.com/orlop/partyclick.git

'''
snapshot.py takes care of the camera logic
'''

# picamera2 is the new libcamera based python library.
# Required for the proper functionality of Raspberry Pi Camera Module v3
from picamera2 import Picamera2
import subprocess
import time

from flash import flash




# snap() takes a picture, saves it and outputs through HDMI
def snap(picam2, capture_filename):
    # define camera
    picam2 = picam2

    picam2.capture_file(capture_filename)
    time.sleep(1)

    # Execute bash command fbi to send the photo to the HDMI (--vt 1) output
    bashCommand = "sudo fbi --autozoom --noverbose --vt 1 /home/partyclick/shared/snapshot.jpg"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()