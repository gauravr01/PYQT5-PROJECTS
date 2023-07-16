from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QGridLayout,QLabel
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
     
        #def a counter of whoe turn it is
        self.counter = 0

        uic.loadUi("tictacto.ui",self)
        self.grid =self.findChild(QGridLayout,"gridLayout")
        self.bt1=self.findChild(QPushButton,"pushButton_1")
        self.bt2=self.findChild(QPushButton,"pushButton_2")
        self.bt3=self.findChild(QPushButton,"pushButton_3")
        self.bt4=self.findChild(QPushButton,"pushButton_4")
        self.bt5=self.findChild(QPushButton,"pushButton_5")
        self.bt6=self.findChild(QPushButton,"pushButton_6")
        self.bt7=self.findChild(QPushButton,"pushButton_7")
        self.bt8=self.findChild(QPushButton,"pushButton_8")
        self.bt9=self.findChild(QPushButton,"pushButton_9")
        self.bt10=self.findChild(QPushButton,"pushButton_10")
        self.label=self.findChild(QLabel,"label")

        self.bt1.clicked.connect(lambda:self.clicker(self.bt1))
        self.bt2.clicked.connect(lambda:self.clicker(self.bt2))
        self.bt3.clicked.connect(lambda:self.clicker(self.bt3))
        self.bt4.clicked.connect(lambda:self.clicker(self.bt4))
        self.bt5.clicked.connect(lambda:self.clicker(self.bt5))
        self.bt6.clicked.connect(lambda:self.clicker(self.bt6))
        self.bt7.clicked.connect(lambda:self.clicker(self.bt7))
        self.bt8.clicked.connect(lambda:self.clicker(self.bt8))
        self.bt9.clicked.connect(lambda:self.clicker(self.bt9))
        self.bt10.clicked.connect(self.reset)


        self.show()
    def checkWin(self): 
        #Across
        if self.bt1.text() != "" and self.bt1.text()== self.bt4.text()and self.bt1.text()== self.bt7.text():
            self.Win(self.bt1,self.bt4,self.bt7)
        if self.bt2.text() != "" and self.bt2.text()== self.bt5.text()and self.bt2.text()== self.bt8.text():
            self.Win(self.bt2,self.bt5,self.bt8)
        if self.bt3.text() != "" and self.bt3.text()== self.bt6.text()and self.bt3.text()== self.bt9.text():
            self.Win(self.bt3,self.bt6,self.bt9)
        #Down
        if self.bt1.text() != "" and self.bt1.text()== self.bt2.text()and self.bt1.text()== self.bt3.text():
            self.Win(self.bt1,self.bt2,self.bt3)
        if self.bt4.text() != "" and self.bt4.text()== self.bt5.text()and self.bt4.text()== self.bt6.text():
            self.Win(self.bt4,self.bt5,self.bt6)
        if self.bt7.text() != "" and self.bt7.text()== self.bt8.text()and self.bt7.text()== self.bt9.text():
            self.Win(self.bt7,self.bt8,self.bt9) 

        #Diagonal
        if self.bt1.text() != "" and self.bt1.text()== self.bt5.text()and self.bt1.text()== self.bt9.text():
            self.Win(self.bt1,self.bt5,self.bt9)
        if self.bt3.text() != "" and self.bt3.text()== self.bt5.text()and self.bt3.text()== self.bt7.text():
            self.Win(self.bt3,self.bt5,self.bt7)
        


    def Win(self,a,b,c): 
        #change the button color
        a.setStyleSheet('QPushButton {color :red ;}')
        b.setStyleSheet('QPushButton {color :red ;}')
        c.setStyleSheet('QPushButton {color :red ;}')
        self.label.setText(f"{a.text()} Wins")

        #Disable the board
        self.disable()

    def disable(self):

        button_list = [
            self.bt1,
            self.bt2,
            self.bt3,
            self.bt4,
            self.bt5,
            self.bt6,
            self.bt7,
            self.bt8,
            self.bt9,
        ]    
        for b in button_list:
           
            b.setEnabled(False)  
    def clicker(self,b):
        if self.counter % 2 == 0:
            mark = "X"
            self.label.setText("O's Turn ")
        else:
            mark = "O"
            self.label.setText("X's Turn ")
        b.setText(mark)
        b.setEnabled(False)
        b.setStyleSheet('QPushButton {color :#797979 ;}')

        self.checkWin()

        #increment counter
        self.counter += 1 

    def reset(self):
        button_list = [
            self.bt1,
            self.bt2,
            self.bt3,
            self.bt4,
            self.bt5,
            self.bt6,
            self.bt7,
            self.bt8,
            self.bt9,
        ]    
        for b in button_list:
            b.setText("")
            b.setEnabled(True)
        
        #reset the button
        self.label.setText("X Goes First")

        #reset the Counter
        self.counter = 0

        self.show()
  
 
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()