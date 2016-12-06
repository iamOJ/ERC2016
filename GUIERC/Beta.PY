import os
import sys
import threading
import msvcrt
import serial
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "guierc.ui" 
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
ardi= serial.Serial('com4',9600)
ardi.close()
ardi.open()


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.settings_button.clicked.connect(self.advanced_settings)
    def advanced_settings(self):
        os.system('adv_sett.py')




class myThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
       key_stroks()



def key_stroks():
    while True:
        
        if msvcrt.kbhit():
            key1=msvcrt.getch()
            
            if key1=='w':
                ardi.write('1')
            if key1=='s':
                ardi.write('2')
            if key1=='a':
                ardi.write('3')
            if key1=='d':
                ardi.write('4')
            
            
           

                
thread_for_keystrokes=myThread()
thread_for_keystrokes.start()
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
