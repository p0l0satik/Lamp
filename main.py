from machine import Pin
import neopixel
from time import sleep

n = 10
def set_all(color):
    for i in range(n):
        np[i] = color
    
def light(color):
    set_all(color)
    np.write()

def travel(color1, color2, speed):
    pos = 0
    while 1:
        set_all(color1)
        np[pos] = color2
        np[pos+1] = color2
        np.write()
        if (pos + 1 < n - 1):
            pos += 1
        else:
            pos = 0
        sleep(speed)

test = Pin(2, Pin.OUT)
test(0)
np = neopixel.NeoPixel(machine.Pin(14),n)
red = (32, 0, 0)
green = (0, 40, 0)
blue = (0, 0, 128)
crimson = (220, 10, 30)
hotpink = (128,52, 90)
orange = (255, 69, 0)
darkorchid = (153, 50, 204)
deepskyblue = (0, 191, 255)
blue_gr = (31, 58, 61)
drozd = (15, 80, 80)
cols = [orange, crimson, blue, deepskyblue]
travel(drozd, orange, 5)
# while 1:
#     for col in cols:
#         set_all(col, np.n)
#         sleep(2)
k, j = 0, 0
# for i in range(110):
#     now = (i, k, j)
#     k += 1
#     j += 1
#     set_all(now, np.n)
#     sleep(0.1)
