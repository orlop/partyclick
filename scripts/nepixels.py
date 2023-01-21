# Daniel Severa, Jr., TWK 2023
# a part of the Diffusionbooth/Partyclick project
# https://github.com/orlop/partyclick.git

'''
neopixels.py takes care of the Adafruit Neopixels logic
'''


import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 15)


pixels[0] = (255, 0, 0)
