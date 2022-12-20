from machine import Pin
import neopixel
from time import sleep

n = 10
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
def set_all(np, color):
    for i in range(n):
        np[i] = color
    
def light(np, color):
    set_all(color)
    np.write()

def travel(np, color1, color2, speed):
    pos = 0
    while 1:
        set_all(np, color1)
        np[pos] = color2
        np[pos+1] = color2
        np.write()
        if (pos + 1 < n - 1):
            pos += 1
        else:
            pos = 0
        sleep(speed)

def set_rainbow(np):
    hotpink = (128,52, 90)
    drozd = (15, 80, 80)
    np[0] = (32, 0, 0)
    np[1] = hotpink
    np[2] = (32, 20, 0)
    np[3] = (32, 32, 0)
    np[4] = (15, 32, 15)
    np[5] = (0, 32, 0)
    np[6] = drozd
    np[7] = (8, 21, 32)
    np[8] = (0, 0, 32)
    np[9] = (17, 0, 32)
    np.write()

if __name__ == "__main__":
    test = Pin(2, Pin.OUT)
    test(0)
    np = neopixel.NeoPixel(machine.Pin(14),n)
    
    cols = [orange, crimson, blue, deepskyblue]
    set_rainbow(np)
    # travel(np, drozd, orange, 5)
