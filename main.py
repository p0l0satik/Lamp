from machine import Pin
import neopixel
from colors import *
from animations import *


if __name__ == "__main__":
    test = Pin(2, Pin.OUT)
    test(0)
    np = neopixel.NeoPixel(machine.Pin(14),n)
    set_orange_pastel_blue(np)
