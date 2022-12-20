from time import sleep
from colors import * 
n = 10
def set_all(np, color):
    for i in range(n):
        np[i] = color
    
def light(np, color):
    set_all(np, color)
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

def set_orange_pastel_blue(np):
    light(np, pastel_blue)
    np[0] = orange
    np[4] = orange
    np[5] = orange
    np[9] = orange
    np.write()