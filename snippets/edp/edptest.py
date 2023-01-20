import digitalio
import busio
import board
from adafruit_epd.epd import Adafruit_EPD

from adafruit_epd.il0373 import Adafruit_IL0373 # The low-res Tri-Color display drivers

# set up EDP pin assignments
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
ecs = digitalio.DigitalInOut(board.CE0)
dc = digitalio.DigitalInOut(board.D22)
rst = digitalio.DigitalInOut(board.D27)
busy = digitalio.DigitalInOut(board.D17)
srcs = None # no need for SRAM, since Raspi has plenty

# initialize the EDP
display = Adafruit_IL0373(152, 152, spi, cs_pin=ecs, dc_pin=dc, sramcs_pin=srcs, rst_pin=rst, busy_pin=busy)


# draw simple shapes
display.rotation = 2
display.fill(Adafruit_EPD.WHITE)

display.fill_rect(20, 20, 50, 60, Adafruit_EPD.RED)
display.hline(80, 30, 60, Adafruit_EPD.BLACK)
display.vline(80, 30, 60, Adafruit_EPD.BLACK)

display.display() # update the EDP