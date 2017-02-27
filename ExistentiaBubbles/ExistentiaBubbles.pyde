'''
Adventures in Processing

Square flight patterns, but like existential stained-glass windows
that grow and then are born again

Author: Kelly Ogilvie
'''
import random
numCir = random.randrange(500)
Crclz = []
deltaX = 0
deltaY = 0
deltaW = 0
deltaH = 0
opacity = 30


def setup():
    size(1200, 1200)
    smooth()
    frameRate(30)
    makeCrclz()
    noStroke()

    
def draw():
    global deltaX
    global deltaY
    global deltaW
    global deltaH
    global Crclz
    background(25)
    pushMatrix()
    drawMovedCrclz()
    for i in range(0,len(Crclz)):                
        if Crclz[i][2] <= 125:
            Crclz[i][2] += 1
            Crclz[i][3] += 1
        elif Crclz[i][2] > 125:
             Crclz[i][2] -= 120
             Crclz[i][3] -= 120
             
             Crclz[i][0] = mouseX + random.uniform(-50,50)
             Crclz[i][1] = mouseY + random.uniform(-50,50)
    popMatrix()


def drawMovedCrclz():
    global Crclz
    global opacity
    pushMatrix()
    for i in range(0,len(Crclz)):
        ellipse(Crclz[i][0],Crclz[i][1],Crclz[i][2],Crclz[i][3])
        fill(Crclz[i][4],Crclz[i][5],Crclz[i][6],opacity)
        #strokeWeight(Crclz[i][7])
    popMatrix()

    
def makeCrclz():
    global Crclz
    for i in range(1, numCir):
        pallette = [[255,0,0],[255,255,255],[120,120,120],[200,200,200]]
        rando = random.randrange(0, 3)
        r = pallette[rando][0]
        g = pallette[rando][1]
        b = pallette[rando][2]
        w = random.randrange(0, 250)
        h = w   # random.randrange(0, 250)
        x = random.randrange(25+w, 1175-w)
        y = random.randrange(25+h, 1175-h)
        cir = [x,y,w,h,r,g,b]
        ellipse(x,y,w,h)
        fill(r,g,b,opacity)
        Crclz.append(cir)