
import random
from gl import Renderer

windoWidth = 1920*1
windowHeight = 1080*1
scale= 1
viewportWidth= windoWidth*scale
viewportHeight= windowHeight *scale
viewportX=0
viewportY=0



myRenderer = Renderer(windoWidth, windowHeight)
myRenderer.glViewPort(viewportX,viewportY,viewportWidth,viewportHeight)




#drawflag()
def abrstractForms():
    originX = windoWidth/2
    originY = windowHeight/2
    destinationX = random.randint(0,windoWidth)
    destinationY = random.randint(0,windowHeight)

    for i in range (20):
        scale = random.random()
        myRenderer.glColor(scale,0.7,0.8)
        sense = random.randint(-1,1)
        strokes= random.randint(20,70)
        for i in range (strokes):        
            myRenderer.glLine(originX,originY,sense*destinationX+(4*i),sense*destinationY-(4*i))
            if (i==49) :

                originX, originY = destinationX,destinationY
                destinationX = random.randint(0,windoWidth)
                destinationY = random.randint(0,windowHeight)




def triangle(x0,y0,x1,y1,x2,y2):


    myRenderer.glLine(x0,y0,x1,y1)
    myRenderer.glLine(x1,y1,x2,y2)
    myRenderer.glLine(x0,y0,x2,y2)


# triangle(0,0,450,450,450,0)


abrstractForms()
#myRenderer.show()
myRenderer.glFinish("output.bmp")