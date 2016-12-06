import pygame
import msvcrt
import sys
from PyQt4 import QtCore, QtGui, uic
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
target=[]
danger = open("danger.txt","w")
qtCreatorFile = "virtual_simulation.ui" # Enter file here.
Ui_MainWindow1, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtGui.QMainWindow, Ui_MainWindow1):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow1.__init__(self)
        self.setupUi(self)
        self.start_v_simulation.clicked.connect(self.start_simulation)
    def start_simulation(self):
        mx=int(self.Xbox.text())
        my=int(self.Ybox.text())
        a=float(self.tx1.text())
        b=float(self.ty1.text())
        target.append((a,b))
        a=float(self.tx2.text())
        b=float(self.ty2.text())
        target.append((a,b))
        a=float(self.tx3.text())
        b=float(self.ty3.text())
        target.append((a,b))
        a=float(self.tx4.text())
        b=float(self.ty4.text())
        target.append((a,b))
        a=float(self.tx5.text())
        b=float(self.ty5.text())
        target.append((a,b))
        self.close()
        gride_online(mx,my)
        
vertices=[]
u=0
b=0



def gride(maxx,maxy):
    
    for i in range(0,maxx+1):
        for j in range(0,maxy+1):
            vertices.append((i,j))
    edge=[]
    j=0
    while j<(maxx+1)*(maxy+1):
        for i in range(0,maxx):
            edge.append((j+i,j+i+1))
        j=j+maxx+1
    j=0
    while j<(maxx+1)*(maxy+1):
        if((j+maxx+1)<((maxx+1)*(maxy+1))):
            edge.append((j,j+maxx+1))
        j=j+1


    glBegin(GL_LINES)
    glColor3fv((1,1,1))
    for e in edge:
        for v in e:
            glVertex2fv(vertices[v])
    glEnd()
    
def rover(x,y):
    ver_main=[(x-0.33,y+0.5),
              (x+0.33,y+0.5),
              (x+0.33,y-0.5),
              (x-0.33,y-0.5)
              
              ]
    surface=[(0,1,2,3)]
    glBegin(GL_QUADS)
    for s in surface:
        glColor3fv((0,0,1))
        for v in s:
            glVertex2fv(ver_main[v])
    glEnd()
    ver_w1=[(x+0.37,y+0.125),
            (x+0.37,y-0.125),
            (x+0.67,y-0.125),
            (x+0.67,y+0.125),
            (x+0.37,y+0.125+0.5),
            (x+0.37,y-0.125+0.5),
            (x+0.67,y-0.125+0.5),
            (x+0.67,y+0.125+0.5),
            (x+0.37,y+0.125-0.5),
            (x+0.37,y-0.125-0.5),
            (x+0.67,y-0.125-0.5),
            (x+0.67,y+0.125-0.5),
            (x-0.37,y+0.125),
            (x-0.37,y-0.125),
            (x-0.67,y-0.125),
            (x-0.67,y+0.125),
            (x-0.37,y+0.125+0.5),
            (x-0.37,y-0.125+0.5),
            (x-0.67,y-0.125+0.5),
            (x-0.67,y+0.125+0.5),
            (x-0.37,y+0.125-0.5),
            (x-0.37,y-0.125-0.5),
            (x-0.67,y-0.125-0.5),
            (x-0.67,y+0.125-0.5)]
    wedge=[(0,1,2,3),
           (4,5,6,7),
           (8,9,10,11),
           (12,13,14,15),
           (16,17,18,19),
           (20,21,22,23)
           ]
    glBegin(GL_QUADS)
    glColor3fv((1,1,0))
    for e in wedge:
        for v in e:
            glVertex2fv(ver_w1[v])
    glEnd()

    
              
def gride_online(maxx,maxy):
    pygame.init()
    display=(800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45,1.333,0.1,500.0)
    glTranslate(-5,-4,-20)
    glRotatef(0,0,0,10)
    u=0
    b=0

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        if msvcrt.kbhit():
            key=msvcrt.getch()
            if key=='w':
                b=b+0.1
            if key=='s':
                b=b-0.1
            if key=='a':
                u=u-0.1
            if key=='d':
                u=u+0.1
            if key=='o':
                a='('+str(u)+','+str(b)+')'+'\n'
                danger.write(a)
            
                
        gride(maxx,maxy)
        rover(u,b)
        glPointSize(6)
        glBegin(GL_POINTS)
        glColor3fv((0,0,1))
        glVertex2fv((9,2))
        glVertex2fv((9.1,2.1))
        glVertex2fv((9.2,2.2))
        glVertex2fv((9.3,2.3))
        glEnd()
        pygame.display.flip()
        pygame.time.wait(10)


def main():
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


main()









        
        
