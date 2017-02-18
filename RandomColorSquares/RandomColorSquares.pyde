'''
Adventures in Processing

Random color squares mapped in duodenary
space-time linguistics

Author: Kelly Ogilvie
'''
import random
size(1200, 1200)
fill(255, 255, 255)
rect(0, 0, 1200, 1200)
#noFill()
strokeWeight(2)
i=1200
while (i > 0):
    op=25
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    fill(r, g, b, op)
    if (i%3 == 0):
        rect(0,0,i,i)
    i=i/2