armAngle = 0
angleChange = 5
ANGLE_LIMIT = 135

def setup():
  size(200, 200)
  smooth()
  frameRate(30)

def draw():
    global armAngle, angleChange, ANGLE_LIMIT
    print armAngle
    background(255)
    pushMatrix()
    translate(50, 50)       # place robot so arms are always on screen
    drawRobot()
    armAngle += angleChange
  
    # if the arm has moved past its limit,
    # reverse direction and set within limits.
    if (armAngle > ANGLE_LIMIT or armAngle < 0):
        angleChange = -angleChange
        armAngle += angleChange
    popMatrix()


def drawRobot():
    noStroke()
    fill(38, 38, 200)
    rect(20, 0, 38, 30)     # head
    rect(14, 32, 50, 50)    # body
    drawLeftArm()
    drawRightArm()
    rect(22, 84, 16, 50)    # left leg
    rect(40, 84, 16, 50)    # right leg
    
    fill(222, 222, 249)
    ellipse(30, 12, 12, 12) # left eye
    ellipse(47, 12, 12, 12) # right eye

def drawLeftArm():
    global armAngle
    pushMatrix()
    translate(12, 32)

    rotate(radians(armAngle))

    rect(-12, 0, 12, 37)    # left arm
    popMatrix()

def drawRightArm():
    global armAngle
    pushMatrix()
    translate(66, 32)

    rotate(radians(-armAngle))

    rect(0, 0, 12, 37)     # right arm
    popMatrix()