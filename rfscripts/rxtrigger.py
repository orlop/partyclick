# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
rxPin = 10 # Broadcom pin 15 (Pi pin 10) - UART RX

# Pin Setup:
GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme    
GPIO.setup(rxPin, GPIO.IN) # Button pin set as input w/ pull-up

# Read GPIO
print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        print(GPIO.input(rxPin))
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
