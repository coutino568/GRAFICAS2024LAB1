
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




# #drawflag()
# def abrstractForms():
#     originX = windoWidth/2
#     originY = windowHeight/2
#     destinationX = random.randint(0,windoWidth)
#     destinationY = random.randint(0,windowHeight)

#     for i in range (20):
#         scale = random.random()
#         myRenderer.glColor(scale,0.7,0.8)
#         sense = random.randint(-1,1)
#         strokes= random.randint(20,70)
#         for i in range (strokes):        
#             myRenderer.glLine(originX,originY,sense*destinationX+(4*i),sense*destinationY-(4*i))
#             if (i==49) :

#                 originX, originY = destinationX,destinationY
#                 destinationX = random.randint(0,windoWidth)
#                 destinationY = random.randint(0,windowHeight)




# def triangle(punto1,punto2,punto3):

# 	x0=punto1[0]
# 	y0=punto1[1]
# 	x1=punto2[0]
# 	y1=punto2[1]
# 	x2=punto3[0]
# 	y2=punto3[1]
# 	myRenderer.glLine(x0,y0,x1,y1)
# 	myRenderer.glLine(x1,y1,x2,y2)
# 	myRenderer.glLine(x0,y0,x2,y2)





poligono1 = [(165, 380), (185, 360) ,(180, 330) ,(207, 345) ,(233, 330) ,(230, 360) ,(250, 380), (220, 385) ,(205, 410) ,(193, 383)]
poligono2 = [(321, 335) ,(288, 286) ,(339, 251) ,(374, 302)]
poligono3 = [(377, 249), (411, 197) ,(436, 249)]
poligono4 = [(413, 177), (448, 159) ,(502, 88) ,(553, 53), (535, 36) ,(676, 37) ,(660, 52),(750, 145), (761, 179), (672, 192) ,(659, 214) ,(615, 214), (632, 230), (580, 230),(597, 215) ,(552, 214) ,(517, 144) ,(466, 180)]

poligono5 = [(682, 175), (708, 120), (735, 148) ,(739, 170)]




## poligono 1
myRenderer.glColor(0,0.2,0.8)
myRenderer.glTriangleFilled(poligono1[3][0],poligono1[3][1],poligono1[1][0],poligono1[1][1],poligono1[2][0],poligono1[2][1])
myRenderer.glTriangleFilled(poligono1[3][0],poligono1[3][1],poligono1[4][0],poligono1[4][1],poligono1[5][0],poligono1[5][1])
myRenderer.glTriangleFilled(poligono1[5][0],poligono1[5][1],poligono1[6][0],poligono1[6][1],poligono1[7][0],poligono1[7][1])
myRenderer.glTriangleFilled(poligono1[7][0],poligono1[7][1],poligono1[8][0],poligono1[8][1],poligono1[9][0],poligono1[9][1])
myRenderer.glTriangleFilled(poligono1[9][0],poligono1[9][1],poligono1[1][0],poligono1[1][1],poligono1[0][0],poligono1[0][1])

myRenderer.glTriangleFilled(poligono1[1][0],poligono1[1][1],poligono1[3][0],poligono1[3][1],poligono1[5][0],poligono1[5][1])
myRenderer.glTriangleFilled(poligono1[9][0],poligono1[9][1],poligono1[1][0],poligono1[1][1],poligono1[5][0],poligono1[5][1])
myRenderer.glTriangleFilled(poligono1[9][0],poligono1[9][1],poligono1[7][0],poligono1[7][1],poligono1[5][0],poligono1[5][1])





## poligono 2
myRenderer.glColor(0.3,0.96,0.3)
for i in range(0,len(poligono2)):
    myRenderer.glTriangleFilled(poligono2[i][0],poligono2[i][1],
                                poligono2[(i+1)%len(poligono2)][0],poligono2[(i+1)%len(poligono2)][1],
                                poligono2[(i+2)%len(poligono2)][0],poligono2[(i+2)%len(poligono2)][1])
## poligono 3

myRenderer.glColor(0.5,0.5,1)
for i in range(0,len(poligono3)):
    myRenderer.glTriangleFilled(poligono3[i][0],poligono3[i][1],
                                poligono3[(i+1)%len(poligono3)][0],poligono3[(i+1)%len(poligono3)][1],
                                poligono3[(i+2)%len(poligono3)][0],poligono3[(i+2)%len(poligono3)][1])
   



# poligono4:
myRenderer.glColor(1,0.3,0.8)
myRenderer.glTriangleFilled(poligono4[0][0],poligono4[0][1],poligono4[1][0],poligono4[1][1],poligono4[17][0],poligono4[17][1])
myRenderer.glTriangleFilled(poligono4[1][0],poligono4[1][1],poligono4[17][0],poligono4[17][1],poligono4[16][0],poligono4[16][1])
myRenderer.glTriangleFilled(poligono4[1][0],poligono4[1][1],poligono4[16][0],poligono4[16][1],poligono4[2][0],poligono4[2][1])

myRenderer.glTriangleFilled(poligono4[2][0],poligono4[2][1],poligono4[16][0],poligono4[16][1],poligono4[3][0],poligono4[3][1])
myRenderer.glTriangleFilled(poligono4[3][0],poligono4[3][1],poligono4[4][0],poligono4[4][1],poligono4[5][0],poligono4[5][1])
myRenderer.glTriangleFilled(poligono4[3][0],poligono4[3][1],poligono4[6][0],poligono4[6][1],poligono4[5][0],poligono4[5][1])
myRenderer.glTriangleFilled(poligono4[3][0],poligono4[3][1],poligono4[6][0],poligono4[6][1],poligono4[16][0],poligono4[16][1])
myRenderer.glTriangleFilled(poligono4[16][0],poligono4[16][1],poligono4[6][0],poligono4[6][1],poligono4[7][0],poligono4[7][1])
myRenderer.glTriangleFilled(poligono4[7][0],poligono4[7][1],poligono4[8][0],poligono4[8][1],poligono4[9][0],poligono4[9][1])
myRenderer.glTriangleFilled(poligono4[9][0],poligono4[9][1],poligono4[16][0],poligono4[16][1],poligono4[7][0],poligono4[7][1])

myRenderer.glTriangleFilled(poligono4[9][0],poligono4[9][1],poligono4[10][0],poligono4[10][1],poligono4[11][0],poligono4[11][1])
myRenderer.glTriangleFilled(poligono4[11][0],poligono4[11][1],poligono4[12][0],poligono4[12][1],poligono4[13][0],poligono4[13][1])
myRenderer.glTriangleFilled(poligono4[11][0],poligono4[11][1],poligono4[13][0],poligono4[13][1],poligono4[14][0],poligono4[14][1])

myRenderer.glTriangleFilled(poligono4[14][0],poligono4[14][1],poligono4[15][0],poligono4[15][1],poligono4[16][0],poligono4[16][1])
myRenderer.glTriangleFilled(poligono4[14][0],poligono4[14][1],poligono4[11][0],poligono4[11][1],poligono4[16][0],poligono4[16][1])
myRenderer.glTriangleFilled(poligono4[9][0],poligono4[9][1],poligono4[11][0],poligono4[11][1],poligono4[16][0],poligono4[16][1])


## poligono 5

myRenderer.glColor(1,1,1)
myRenderer.glTriangleFilled(poligono5[0][0],poligono5[0][1],poligono5[1][0],poligono5[1][1],poligono5[2][0],poligono5[2][1])
myRenderer.glTriangleFilled(poligono5[0][0],poligono5[0][1],poligono5[3][0],poligono5[3][1],poligono5[2][0],poligono5[2][1])


# abrstractForms()
#myRenderer.show()
myRenderer.glFinish("output.bmp")