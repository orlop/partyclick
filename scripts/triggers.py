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

from rpi_rf import RFDevice

# Define capture variables
square_width=512
#capture_filename="/home/partyclick/shared/RFimage.jpg"
capture_filename="/home/partyclick/shared/fbitest.jpg"


# Threaded callback to monitor physical button press
def arcadebtn_callback(channel):
   print("Arcade button triggered.")
   snap(square_width=square_width,capture_filename=capture_filename) 
   time.sleep(1)  # prevent registering multiple times 


GPIO.add_event_detect(17, GPIO.FALLING, callback=arcadebtn_callback)



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
parser.add_argument('-g', dest='gpio', type=int, default=27, 
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
       print(str(rfdevice.rx_code)) 
       if str(rfdevice.rx_code) == code_of_interest: 
           snap(square_width=square_width,capture_filename=capture_filename) 
           time.sleep(1)  # prevent registering multiple times 
   time.sleep(0.01) 
rfdevice.cleanup()