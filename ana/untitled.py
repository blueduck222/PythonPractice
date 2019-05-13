import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("untitled.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 할당하는 코드
       
        self.lineEdit.returnPressed.connect(self.printTextFunction)
        self.lineEdit.textChanged.connect(self.changeTextFunction)
        self.plainTextEdit.textChanged.connect(self.changestoryFunction)

    def printTextFunction(self) :
       
        print(self.lineEdit.text())

    def changeTextFunction(self) :
       
        self.label.setText(self.lineEdit.text())

    def changestoryFunction(self) :

        self.textBrowser.setPlainText(self.plainTextEdit.toPlainText())

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()