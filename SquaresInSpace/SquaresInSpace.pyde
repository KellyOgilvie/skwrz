'''
Adventures in Processing

Maps Squares to L-dimensional space, according to the laws of 
Blakian geometry.

An explanation of the algorithm:
    Assume squares are drawn clockwise
    and consist of four sets of vertices
    x1-4, y1-4. 
    
    Always:
    x2 > x1
    x3 > x2
    x4 < x3 
    
    Conditionally:
    if y2 > y1
    y3 > y2
    y4 < y3
    else
    y3 < y2
    y4 > y3
        

Author: Kelly Ogilvie
'''
import random
numSqr = 10
Sqrz = []
a = 25 #opacity channel

def setup():
    size(1200,1200)
    background(255,255,255)
    strokeWeight(2)
    getVertices()
    print(Sqrz)
    
def draw():
    global Sqrz
    for i in range(0,len(Sqrz)):
        x1 = Sqrz[i][0]
        y1 = Sqrz[i][1]
        x2 = Sqrz[i][2]
        y2 = Sqrz[i][3]
        x3 = Sqrz[i][4]
        y3 = Sqrz[i][5]
        x4 = Sqrz[i][6]
        y4 = Sqrz[i][7]
        r = Sqrz[i][8]
        g = Sqrz[i][9]
        b = Sqrz[i][9]
        beginShape()
        vertex(x1,y1)
        vertex(x2,y2)
        vertex(x3,y3)
        vertex(x4,y4)
        vertex(x1,y1)
        endShape()
        fill(r,g,b,a)

    
def getVertices():
    global Sqrz
    global numSqr
    sqrlst = []
    for i in range(0,numSqr):
        x1 = random.randrange(100,200)
        x2 = random.randrange(100,200) + x1
        x3 = random.randrange(100,200) + x2
        x4 = random.randrange(100,200) - 10#x3

        y1 = random.randrange(100,200)
        y2 = random.randrange(100,200)
        if y2 > y1:
            y3 = random.randrange(100,200) + y2
            y4 = random.randrange(100,200) - 10#y3
        else:
            y3 = random.randrange(100,200) - 10#y2
            y4 = random.randrange(100,200) + y3
        col = getRandomColor()
        r = col[0]
        g = col[1]
        b = col[2]
        sqrlst = [x1,y1,x2,y2,x3,y3,x4,y4,r,g,b]
        Sqrz.append(sqrlst)
    
def getRandomColor():
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    return(r,g,b)