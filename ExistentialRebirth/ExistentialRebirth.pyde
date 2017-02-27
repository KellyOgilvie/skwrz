'''
Adventures in Processing

Square flight patterns, but like existential stained-glass windows
that grow and then are born again

Author: Kelly Ogilvie
'''
import random
numSqr = random.randrange(300, 500)
Sqrz = []
deltaX = 0
deltaY = 0
deltaS = 0
deltaW = 0
deltaH = 0
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
    global deltaW
    global deltaH
    global Sqrz
    background(255)
    pushMatrix()
    drawSqrz()
    for i in range(0,len(Sqrz)):
        #deltaX = random.uniform(-3,3)
        #deltaY = random.uniform(-3,3)
        #Sqrz[i][0] += deltaX
        #Sqrz[i][1] += deltaY
        
        #deltaS = random.uniform(-3,3)
        #if (Sqrz[i][7] + deltaS >= 0) and (Sqrz[i][7] + deltaS <= 3):
        #    Sqrz[i][7] += deltaS
            
        if Sqrz[i][2] <= 125:
            Sqrz[i][2] += 12
        elif Sqrz[i][2] > 125:
             Sqrz[i][2] -= 120
             deltaX = random.uniform(-300,300)
             deltaY = random.uniform(-300,300)
             Sqrz[i][0] += deltaX
             Sqrz[i][1] += deltaY

        
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
        pallette = [[255,0,0],[20,20,20],[120,120,120],[200,200,200]]
        rando = random.randrange(0, 3)
        r = pallette[rando][0]
        g = pallette[rando][1]
        b = pallette[rando][2]
        w = random.randrange(0, 250)
        h = random.randrange(0, 250)
        x = random.randrange(25+w, 1175-w)
        y = random.randrange(25+h, 1175-h)
        #s = random.randrange(1,3)
        sqr = [x,y,w,h,r,g,b]
        rect(x,y,w,h)
        fill(r,g,b,opacity)
        Sqrz.append(sqr)