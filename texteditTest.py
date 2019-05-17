import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("texteditTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.fontSize = 10

        #TextEdit과 관련된 버튼에 기능 연결
        self.btn_printTextEdit.clicked.connect(self.printTextEdit)
        self.btn_clearTextEdit.clicked.connect(self.clearTextEdit)
        self.btn_setFont.clicked.connect(self.setFont)
        self.btn_setFontItalic.clicked.connect(self.fontItalic)
        self.pushButton.clicked.connect(self.lineEdittext)
        self.pushButton_2.clicked.connect(self.fontSizeFunc)
       
    def printTextEdit(self) :
        print(self.textedit_Test.toPlainText())

    def clearTextEdit(self) :
        self.textedit_Test.clear()

    def setFont(self) :
        fontvar = QFont("굴림",10)
        self.textedit_Test.setCurrentFont(fontvar)

    def fontItalic(self) :
        self.textedit_Test.setFontItalic(True)

    def lineEdittext(self) :
        a = self.lineEdit_2.text()
        a = a.split(' ')
        colorvar = QColor(int(a[0]),int(a[1]),int(a[2]),int(a[3]))
        self.textedit_Test.setTextColor(colorvar)

    def fontSizeFunc(self) :
        size = int(self.lineEdit_3.text())
        self.textedit_Test.setFontPointSize(size)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 