'''
Adventures in Processing

Square flight patterns, but like existential stained-glass windows

Author: Kelly Ogilvie
'''
import random
numSqr = random.randrange(300, 500)
Sqrz = []
deltaX = 0
deltaY = 0
#deltaS = 0
opacity = 30


def setup():
    size(1200, 1200)
    smooth()
    frameRate(30)
    makeSqrz()
    noStroke()

    
def draw():
    global deltaX
    global deltaY
    global Sqrz
    background(255)
    pushMatrix()
    drawSqrz()
    for i in range(0,len(Sqrz)):
        deltaX = random.uniform(-3,3)
        deltaY = random.uniform(-3,3)
        Sqrz[i][0] += deltaX
        Sqrz[i][1] += deltaY
        #deltaS = random.uniform(-3,3)
        #if (Sqrz[i][7] + deltaS >= 0) and (Sqrz[i][7] + deltaS <= 3):
            #Sqrz[i][7] += deltaS
    popMatrix()
    
def drawSqrz():
    global Sqrz
    drawMovedSqr()

def drawMovedSqr():
    global Sqrz
    global opacity
    pushMatrix()
    for i in range(0,len(Sqrz)):
        rect(Sqrz[i][0],Sqrz[i][1],Sqrz[i][2],Sqrz[i][3])
        fill(Sqrz[i][4],Sqrz[i][5],Sqrz[i][6],opacity)
        #strokeWeight(Sqrz[i][7])
    popMatrix()

    
def makeSqrz():
    global Sqrz
    for i in range(1, numSqr):
        r = random.randrange(0, 255)
        g = random.randrange(0, 255)
        b = random.randrange(0, 255)
        w = random.randrange(0, 250)
        h = random.randrange(0, 250)
        x = random.randrange(25+w, 1175-w)
        y = random.randrange(25+h, 1175-h)
        #s = random.randrange(1,3)
        sqr = [x,y,w,h,r,g,b]
        rect(x,y,w,h)
        fill(r,g,b,opacity)
        Sqrz.append(sqr)