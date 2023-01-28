# Daniel Severa, Jr., TWK 2023
# a part of the Diffusionbooth/Partyclick project
# https://github.com/orlop/partyclick.git

# triggers.py takes care of triggering the process through RF or wired buttons

from snapshot import snap

import argparse
import signal
import sys
import time
import logging

import RPi.GPIO as GPIO
from rpi_rf import RFDevice
from picamera2 import Picamera2
from libcamera import Transform
from flash import flash_off, flash_on



# Define capture variables
square_width=512
capture_filename="/home/partyclick/shared/snapshot.jpg"

RFPin = 23 # Data pin (yellow wire) for the RF receiver
ArcadeBtnPin = 16 # Pulldown pin (green wire) for the Arcade Button

#ahoj
# set up camera
picam2 = Picamera2()
# Start the camera with the config and no preview
preview_config = picam2.create_preview_configuration(transform=Transform(vflip=True))
picam2.configure(preview_config)
picam2.preview_configuration.main.size = (square_width, square_width) # set capture size
picam2.start(show_preview=False)

# se tup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(ArcadeBtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # GPIO BCM Pin 17 = Board Pin 11
#GPIO.setup(RFPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set up as an input


# Threaded callback to monitor physical button press
def arcadebtn_callback(channel):
   print("Arcade button triggered.")
   snap(picam2=picam2, capture_filename=capture_filename) 
   time.sleep(1)  # prevent registering multiple times 


GPIO.add_event_detect(ArcadeBtnPin, GPIO.FALLING, callback=arcadebtn_callback) # Watch for GPIO 17 to be grounded and call arcadebtn_callback()



# The main thread listens for RF signals
#       The signals generated by my keychain are:
#        5518280 [pulselength 329, protocol 1] (red button A)
#        5518276 [pulselength 328, protocol 1] (grey button B)
rfdevice = None

def exithandler(signal, frame): 
   rfdevice.cleanup() 
   sys.exit(0) 

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S', 
                   format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', ) 
parser = argparse.ArgumentParser(description='Receives a decimal code via a 433/315MHz GPIO device') 
parser.add_argument('-g', dest='gpio', type=int, default=RFPin, 
                   help="GPIO pin (Default: 27)") 
args = parser.parse_args() 
signal.signal(signal.SIGINT, exithandler) 
rfdevice = RFDevice(args.gpio) 
rfdevice.enable_rx() 
timestamp = None 
logging.info("Listening for codes on GPIO " + str(args.gpio)) 
code_of_interest = '5518280' 
#
while True: 
   if rfdevice.rx_code_timestamp != timestamp: 
       timestamp = rfdevice.rx_code_timestamp 
       if str(rfdevice.rx_code) == code_of_interest: 
            flash_on()
            snap(picam2=picam2, capture_filename=capture_filename)
            time.sleep(1)  # prevent registering multiple times 
            flash_off()
            exec(open('scripts/automatic-lambda-img2img.py').read())
            exec(open('scripts/upload-image.py').read())
            exec(open('scripts/epd-pillow-image.py').read())
   time.sleep(0.01) 
rfdevice.cleanup()