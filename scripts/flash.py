# Daniel Severa, Jr., TWK 2023
# a part of the Diffusionbooth/Partyclick project
# https://github.com/orlop/partyclick.git

'''
flash.py takes care of flashing the LEDs
'''

import RPi.GPIO as GPIO
import time

# SET PINS
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT) # BCM pin 21, Board pin 40

def flash():
    print("LED on")
    GPIO.output(21,GPIO.HIGH)
    time.sleep(3)
    print("LED off")
    GPIO.output(21,GPIO.LOW)


def flash_on():
    print("LED on")
    GPIO.output(21,GPIO.HIGH)


def flash_off():
    print("LED off")
    GPIO.output(21,GPIO.LOW)