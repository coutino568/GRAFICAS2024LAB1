import struct

def char(c):
    # used to reduce it to 1 byte

    return struct.pack('=c', c.encode('ascii'))

def word(w):
    # used to reduce it to 2 byte
    return struct.pack('=h',w)

def dword(d):
    # used to reduce it to 4 byte
    return struct.pack('=l',d)

def color(r ,g ,b ):
    #takes input from 0 to 1
    return bytes ([ int(b *255), int(g *255), int(r*255)])



class Renderer(object):
    def __init__(self,width , height):
        self.black = color(0,0,0)
        self.bgColor = color(0,0,0)
        self.viewportBgColor = color(1,1,1)
        self.mainColor = color(0,0,0)
        self.glCreateWindow( width, height)
        self.glViewPort(0,0,self.width,self.height)
        



    def glCreateWindow (self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.glClear()    
    

    def glViewPort(self, x = 0, y=0, width=1, height = 1):
        self.viewportW = int(width)
        self.viewportH = int(height)
        self.viewportX = int(x)
        self.viewportY = int(y)
        print("Viewport is defined from : " + str(x) + " , " + str(y) )
        print("To :  " + str(x+width) + " , " + str(y+height) )
        self.glClear()
        self.glClearviewport()
        


    def pickForegroundColor( self, r,g,b):
        self.mainColor = color(r,g,b)

    def glClear(self):
        self.matrix = [[self.bgColor for x in range(self.width)] for y in range(self.height)]
        


    def glClearviewport(self):

        for x in range (self.viewportX, self.viewportX+ self.viewportW):
            for y in range (self.viewportY, self.viewportY+self.viewportH):
                self.matrix[y][x] = self.viewportBgColor

        


    def glClearColor (self, r,g,b):
        self.bgColor = color(r,g,b)
        
        
    def glStar(self,x,y):
        x=int(x)
        y=int(y)
        if (x>= self.viewportX and x <= (self.viewportX+self.viewportW)  and   y>= self.viewportY and y <= self.viewportY+self.viewportH) :
            self.matrix[y][x] = self.mainColor
            self.matrix[y-1][x] = self.mainColor
            self.matrix[y+1][x] = self.mainColor
            self.matrix[y][x-1] = self.mainColor
            self.matrix[y][x+1] = self.mainColor
            
        # else :
        #     print("point out of viewport")


    def glVertex(self,x,y):
        x=int(x)
        y=int(y)
        if (x>= self.viewportX and x <= (self.viewportX+self.viewportW)  and   y>= self.viewportY and y <= self.viewportY+self.viewportH) :
            self.matrix[y][x] = self.mainColor
        # else :
        #     print("point out of viewport")


    def glVertexNormalized(self,x,y):
        #convertion
        x = int((x+1)*(self.viewportW/2) +self.viewportX)
        y = int((y+1)*(self.viewportH/2) + self.viewportY)

        if (x>= self.viewportX and x <= (self.viewportX+self.viewportW)  and   y>= self.viewportY and y <= self.viewportY+self.viewportH) :
            self.matrix[y][x] = self.mainColor


    def glColor(self, r,g,b):
        self.mainColor = color(r,g,b)


    def glLine(self, x0,y0,x1, y1):

        x0 = int(x0)
        y0 = int(y0)
        x1 = int(x1)
        y1 = int(y1)
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        steep = (dy > dx)
        offset = 0
        limit = 0.1
        
        

        #para pendientes mayores a 1
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
            

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        y = y0
        m = dy/dx

        for x in range(x0, x1 + 1):
            if (steep):
                self.glVertex(y, x)
            else:
                self.glVertex(x, y )

            offset += m
            if offset >= limit:
                y += 1 if y0 < y1 else -1
                limit += 1


        # #asegurar que se dibuje la linea de izqierda a derecha
        # if x0 > x1:
        #     x0, x1 = x1, x0
        #     y0, y1 = y1, y0

    
    def glLine2(self, x0,y0,x1, y1):
        pixeles = []
        x0 = int(x0)
        y0 = int(y0)
        x1 = int(x1)
        y1 = int(y1)
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        steep = (dy > dx)
        offset = 0
        limit = 0.1
        
        
        
        

        #para pendientes mayores a 1
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
            

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        y = y0
        try:
            m = dy/dx
        except:
            m= 0

        for x in range(x0, x1 + 1):
            if (steep):
                pixeles.append([y,x])
            else:
                pixeles.append([x,y])
                

            offset += m
            if offset >= limit:
                y += 1 if y0 < y1 else -1
                limit += 1
        return pixeles
    
    
    
    # def glTriangleFilled(self, x0,y0,x1,y1,x2,y2):
        
    #     maxx= max(x0,x1,x2)
    #     minx= min (x0,x1,x2)
    #     maxy = max (y0,y1,y2)
    #     miny = min (y0,y1,y2)
        
    #     self.glLine(x0,y0,x1,y1)
    #     self.glLine(x0,y0,x2,y2)
    #     self.glLine(x2,y2,x1,y1)
        
        
        
    def glTriangleFilled(self, x0,y0,x1,y1,x2,y2):
        #linea de A a B
        self.glLine(x0,y0,x1,y1)
        #linea de B a C
        self.glLine(x2,y2,x1,y1)
        #linea de A a C
        self.glLine(x0,y0,x2,y2)
        #coleccionar todos los puntos sobre el trazo A a C
        #coleccionar todos los puntos sobre el trazo B a C
        #coleccionar todos los puntos sobre el trazo A a B
        puntos = self.glLine2(x0,y0,x2,y2)
        puntos2= self.glLine2(x1,y1,x2,y2)
        puntos3= self.glLine2(x0,y0,x1,y1)
        #lanzar una linea de B a toda la coleccion de puntos en la linea AC.
        # print(puntos)
        for punto in puntos:
            self.glLine(x1,y1,punto[0],punto[1])
        #lanzar una linea de A a toda la coleccion de puntos en la linea BC.
        for punto in puntos2:
            self.glLine(x0,y0,punto[0],punto[1])
        #lanzar una linea de C a toda la coleccion de puntos en la linea AB.
        for punto in puntos3:
            self.glLine(x2,y2,punto[0],punto[1])
        

    
    def glFinish(self,filename):
        with open(filename, "wb") as file:
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14 + 40 + (self.width * self.height * 3)))
            file.write(dword(0))
            file.write(dword(14 + 40))
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.matrix[y][x])



    def show(self):
        for x in range(self.height):
            print(self.matrix[x])