from PyQt5.QtWidgets import QMainWindow,QApplication,QLCDNumber
from PyQt5 import uic
import sys
from PyQt5.QtCore import QTime, QTimer
from datetime import  datetime
class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        uic.loadUi("watch.ui",self)
        self.lcd = self.findChild(QLCDNumber,"lcdNumber")
        #create a timer
        self.timer =QTimer()
        self.timer.timeout.connect(self.lcd_number)
        #start the timer and update every second
        self.timer.start(1000)
        #Call the lcd function
        self.lcd_number()
        
        self.show()

    def lcd_number(self):
        # Get the time

        time = datetime.now()
        formatted_time= time.strftime("%I:%M:%S")

        #Set the number of LCD digits
        self.lcd.setDigitCount(8)
        #No white border on text(Flat Text)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)  
        #Display the time  
        self.lcd.display(formatted_time)
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()