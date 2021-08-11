from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import Test_window
import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score

class firstwindow(QWidget):
    def __init__(self):
        super(firstwindow, self).__init__()
        self.prepareScreen1()

    def prepareScreen1(self):
        self.setWindowTitle("WELCOME")
        self.setGeometry(30, 50, 1850, 950)
        newfont = QFont("Consolas", 18, QFont.Bold)
        newfont1 = QFont("Times", 30, QFont.StyleItalic, QFont.Bold)
        lbl1 = QLabel('WELCOME TO THE BREAST CANCER DETECTION WINDOW')
        lbl1.setFont(newfont1)
        btn1 = QPushButton("CLICK HERE TO CHECK")
        btn1.setFont(newfont1)

        image = QImage(os.path.abspath("img1.png"))
        sImage = image.scaled(QSize(50, 50))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)


        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(lbl1, 0, 0)
        grid.addWidget(btn1, 1, 0)
        btn1.clicked.connect(self.testing)
        self.setLayout(grid)
        self.show()

    def testing(self):
        try:
            self.obj = Test_window.cancdet()
            self.obj.show()
        except BaseException as ex:
            print(ex)
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = firstwindow()
    sys.exit(app.exec_())


