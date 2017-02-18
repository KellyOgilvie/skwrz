'''
Adventures in Processing

Square flight patterns

Author: Kelly Ogilvie
'''
import random
size(1200, 1200)
fill(255, 255, 255)
opacity = 25
rect(0, 0, 1200, 1200)
strokeWeight(2)
numSqr = random.randrange(20, 150)
for i in range(1, numSqr):
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    x = random.randrange(100, 1100)
    y = random.randrange(100, 1100)
    w = random.randrange(0, 250)
    h = random.randrange(0, 250))
    fill(r, g, b, opacity)
    rect(x, y, w, h)