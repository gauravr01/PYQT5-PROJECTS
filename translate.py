from PyQt5.QtWidgets import QMainWindow,QApplication,QComboBox,QLabel,QPushButton,QTextEdit,QMessageBox
# from PyQt5.QtWidgets import QMainWindow,QApplication,QComboBox,QLabel,QPushButton,QTextEdit,QMessageBox
from PyQt5 import uic
import sys
import googletrans
import textblob

class UI(QMainWindow):

    def __init__(self):
        super(UI,self).__init__()

        uic.loadUi("translate.ui",self)
        
        self.t_button=self.findChild(QPushButton,"pushButton")
        self.c_button=self.findChild(QPushButton,"pushButton_2")
    
        self.combo_1=self.findChild(QComboBox,"comboBox")
        self.combo_2=self.findChild(QComboBox,"comboBox_2")

        self.text_1=self.findChild(QTextEdit,"textEdit")
        self.text_2=self.findChild(QTextEdit,"textEdit_2")


        self.t_button.clicked.connect(self.translate)
        self.c_button.clicked.connect(self.clear)

        # Add languages to the combobox
        self.languages = googletrans.LANGUAGES
        # print(self.languages)
        self.language_list = list(self.languages.values())
        # print(self.language_list)

        #Add items to combo boxes
        self.combo_1.addItems(self.language_list) 
        self.combo_2.addItems(self.language_list )
        
        #default set in combo box
        self.combo_1.setCurrentText("English")
        self.combo_2.setCurrentText("Hindi")


        self.show()
    def clear(self):
        #clear the textboxes
        self.textEdit.setText("")
        self.textEdit_2.setText("")
        
        #reset the combobox
        self.combo_1.setCurrentText("English")
        self.combo_2.setCurrentText("Hindi")
    def translate(self):
        try:
            #Get Original Language key 
            for key,value in self.languages.items():
                if (value == self.combo_1.currentText()):
                    from_language_key = key

            #Get Translated Language key 
            for key,value in self.languages.items():
                if (value == self.combo_2.currentText()):
                    to_language_key = key

            # self.text_1.setText(from_language_key)
            # self.text_2.setText(to_language_key)
            
            #Turn Original text to textblob
            words = textblob.TextBlob(self.text_1.toPlainText())
            #Translate words 
            words = words.translate(from_lang=from_language_key,to=to_language_key)

            #Output in text_2
            self.text_2.setText(str(words))

        except Exception as e:
            QMessageBox.about(self,"Translator",str(e))     
        

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()