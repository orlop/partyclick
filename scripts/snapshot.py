# Daniel Severa, Jr., TWK 2023
# a part of the Diffusionbooth/Partyclick project
# https://github.com/orlop/partyclick.git

# snapshot.py takes care of the camera logic

# picamera2 is the new libcamera based python library.
# Required for the proper functionality of Raspberry Pi Camera Module v3
from picamera2 import Picamera2
import subprocess
import time

# snap() takes a picture, saves it and outputs through HDMI
def snap(square_width, capture_filename):
    size=(square_width,square_width)

    # Build capture config and set capture size
    capture_config = picam2.create_still_configuration()
    capture_config['main']['size'] = size
    print(capture_config)

    # Start the camera with the config and no preview
    picam2.configure(capture_config)
    picam2.start(show_preview=False)


    picam2.capture_file(capture_filename)
    time.sleep(1)
    picam2.stop()

    # Execute bash command fbi to send the photo to the HDMI (--vt 1) output
    bashCommand = "sudo fbi --autozoom --noverbose --vt 1 /home/partyclick/shared/fbitest.jpg"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()