#!/usr/bin/env pythonš
# script to monitor GPIO for RF signals and trigger camera when the right button is pressed
# by Daniel Severa, Jr. | Tweak Post s.r.o., 2023

# dependencies
import RPi.GPIO as GPIO

# se tup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIOPUD_DOWN) # GPIO BCM Pin 27 = Board Pin 11
GPIO.setup(27, GPIO.IN, pull_up_down=GPIOPUD_UP) # GPIO BCM Pin 27 = Board Pin 13

# Threaded Callback
def rf_callback(channel):
    print("GPIO 27 triggered.")

GPIO.add_event_detect(24, GPIO.RISING, calback=rf_callback)

try:
    print("Waiting for a physical button press.")
    GPIO.wait_for_edge(17)
    print("Button pressed.")

except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()