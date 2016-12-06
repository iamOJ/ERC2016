import os
import sys
import threading
import msvcrt
import pygame
import time


pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
print 'Initialized Joystick : %s' %j.get_name()
from PyQt4 import QtCore, QtGui, uic

def get():
    out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    it = 0 #iterator
    pygame.event.pump()
    
    #Read input from the two joysticks       
    for i in range(0, j.get_numaxes()):
        out[it] = j.get_axis(i)
        it+=1
    #Read input from buttons
    for i in range(0, j.get_numbuttons()):
        out[it] = j.get_button(i)
        it+=1
    return out

qtCreatorFile = "guierc.ui" 
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)



class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    con_int=1
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.settings_button.clicked.connect(self.advanced_settings)
        self.virtual_world_button.clicked.connect(self.virtual_world)
        self.control_dropbox.currentIndexChanged.connect(self.change_input)
    def change_input(self):
        current_input=str(self.control_dropbox.currentText())
        

        if current_input=='Keyboard':
            pixmap=QtGui.QPixmap('keyboard_latest.png')
            self.con_int=1
        if current_input=='Controller':
            pixmap=QtGui.QPixmap('game_control.png')
            self.con_int=2
        self.controller_pic.setPixmap(pixmap)
    def advanced_settings(self):
        os.system('adv_sett.py')
    def virtual_world(self):
        os.system('design_alpha.py')

            
           

                

app = QtGui.QApplication(sys.argv)
window = MyApp()
window.show()

def clock_or_anti(co_od,xn,yn,xo,yo):
    a=1
    b=0
    if co_od[7]==1:
        a=2
        
    dx=xn-xo
    dy=yn-yo
    
    if xn>0 and yn>0:#first quadrant
        if dx>0 and dy<0:
            b=1
        if dx<0 and dy>0:
            b=-1
    if xn<0 and yn>0: #second quadrant
        if dx>0 and dy>0:
            b=1
        if dx<0 and dy<0:
            b=-1
    if xn<0 and yn<0: #third quadrant
        if dx>0 and dy<0:
            b=-1
        if dx<0 and dy>0:
            b=1
                
    if xn>0 and yn<0: #forth quadrant
        if dx>0 and dy>0:
            b=-1
        if dx<0 and dy<0:
            b=1
    return (a,b)


class myThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
       key_stroks(window)



def key_stroks(con_window):
    
    actuator1=0
    actuator2=0
    print 'Ready'
    while True:
        while con_window.con_int==1:
            if msvcrt.kbhit():
                key1=msvcrt.getch()
                if key1=='w':
                    print "rover foward"
                if key1=='s':
                    print "rover down"
                if key1=='a':
                    print "rover left"
                if key1=='d':
                    print "rover right"
                if key1=='t':
                    print "actuatorI up"
                    actuator1=actuator1+10
                    con_window.accISlider.setValue(actuator1)
                if key1=='g':
                    print "actuatorI down"
                    if actuator1>=0:
                        actuator1=actuator1-10
                    con_window.accISlider.setValue(actuator1)
                if key1=='u':
                    print "actuatorII up"
                    actuator2=actuator2+10
                    con_window.accIISlider.setValue(actuator2)
                if key1=='j':
                    print "actuatorI down"
                    if actuator2>=0:
                        actuator2=actuator2-10
                    con_window.accIISlider.setValue(actuator2)
        while con_window.con_int==2:
            co_od=get()
            x2n=100*co_od[0]
            y2n=-100*co_od[1]
            x2o=x2n
            y2o=y2n
            while con_window.con_int==2:
                
                r_control=clock_or_anti(co_od,x2n,y2n,x2o,y2o)
                if x2o!=x2n and y2o!=y2n:
                    x2o=x2n
                    y2o=y2n
                
                x=100*co_od[2]
                y=-100*co_od[3]
                if x>0.1 :
                    print "rover right"
                if x<-0.1 :
                    print "rover left"
                if y>0.1:
                    print "rover upward"
                if y<-0.1:
                    print "rover downward"
                if r_control==(1,1):
                    print "robotic arm clockwise"
                if r_control==(1,-1):
                    print "robotic arm anti-clockwise"
                if r_control==(2,1):
                    print "claw clockwise"
                if r_control==(2,-1):
                    print "claw anti-clockwise"
                if co_od[8]==1:
                    print "actuatorI down"
                if co_od[10]==1:
                    print "actuatorI up"
                if co_od[9]==1:
                    print "actuatorII down"
                if co_od[11]==1:
                    print "actuatorII up"
                if co_od[5]==1:
                    print "claw capture"
                    



                time.sleep(0.1)
                co_od=get()
                x2n=100*co_od[0]
                y2n=-100*co_od[1]
            
            

thread_for_keystrokes=myThread()
thread_for_keystrokes.start()        
            


sys.exit(app.exec_())

