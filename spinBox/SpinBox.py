import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("SpinBox.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.list_score = []
        self.list_subject = ["국어","수학","영어","사회","과학"]
        self.addComboBoxItem()

        self.Btn_save.clicked.connect(self.saveclickedFunc)
        self.Btn_see.clicked.connect(self.seeclickedFunc)
        self.Btn_print.clicked.connect(self.printclickedFunc)


    def addComboBoxItem(self) :
        for i in self.list_subject :
            self.comboBox.addItem(i)
            self.list_score.append(0)

    def saveclickedFunc(self):
        self.list_score[self.comboBox.currentIndex()] = self.doubleSpinBox.value()
    
    def seeclickedFunc(self):

        self.textBrowser.clear()

        for i in range(0,len(self.list_subject)) :
            self.textBrowser.append(str(self.list_subject[i]) + str(self.list_score[i]))

    def printclickedFunc(self):
        for i in range(0,len(self.list_subject)) :
            print(str(self.list_subject[i]) + str(self.list_score[i]))


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 