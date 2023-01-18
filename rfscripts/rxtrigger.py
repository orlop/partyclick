#!/usr/bin/env pythonš
# script to monitor GPIO for RF signals and trigger camera when the right button is pressed
# by Daniel Severa, Jr. | Tweak Post s.r.o., 2023

# dependencies
import RPi.GPIO as GPIO

## RX CODE ##
import argparse
import signal
import sys
import time
import logging

from rpi_rf import RFDevice

rfdevice = None

# pylint: disable=unused-argument
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

## END OF RX CODE ##


# se tup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) # GPIO BCM Pin 17 = Board Pin 11
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_OFF) # GPIO BCM Pin 27 = Board Pin 13

# Threaded Callback
def rf_callback(channel):
    print("GPIO 27 triggered.")
    print(rfdevice.rx_code)


GPIO.add_event_detect(27, GPIO.RISING, callback=rf_callback)

try:
    print("Waiting for a physical button press.")
    GPIO.wait_for_edge(17, GPIO.FALLING)
    print("Button pressed.")

except KeyboardInterrupt:
    GPIO.cleanup()
    rfdevice.cleanup()
GPIO.cleanup()
rfdevice.cleanup()