'''
Adventures in Processing

Square flight patterns, but like, lots of them

Author: Kelly Ogilvie
'''
import random
size(1200, 1200)
fill(255, 255, 255)
opacity = 25
rect(0, 0, 1200, 1200)
strokeWeight(2)
t = 0
while(t < 10):
    numSqr = random.randrange(20, 150)
    for i in range(1, numSqr):
        r = random.randrange(0, 255)
        g = random.randrange(0, 255)
        b = random.randrange(0, 255)
        w = random.randrange(0, 250)
        h = random.randrange(0, 250)
        x = random.randrange(25+w, 1175-w)
        y = random.randrange(25+h, 1175-h)
        fill(r, g, b, opacity)
        rect(x, y, w, h)
    t = t+1
    redraw()