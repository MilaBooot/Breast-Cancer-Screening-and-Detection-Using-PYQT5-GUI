from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from utilities import  *
from sklearn.metrics import accuracy_score

class cancdet(QWidget):
    def __init__(self):
        super(cancdet, self).__init__()
        self.prepareScreen()

    def prepareScreen(self):
        self.setWindowTitle("Cancer Detection")
        self.setGeometry(30, 50, 1850, 950)
        newfont = QFont("Consolas", 18, QFont.Bold)
        newfont2 = QFont("Consolas", 14, QFont.Bold)
        newfont1 = QFont("Consolas", 20, QFont.StyleItalic, QFont.Bold)
        lbl1 = QLabel('Clump_thickness:')
        lbl2 = QLabel("Uniform_Cell_Size:")
        lbl3 = QLabel('Uniform_Cell_Shape:')
        lbl4 = QLabel('Marginal_Adhesion:')
        lbl5 = QLabel("Single_Apithelial_Size:")
        lbl6 = QLabel('Bare_Nuclei:')
        lbl7 = QLabel('Bland_Chromatin:')
        lbl8 = QLabel("Normal_Nucleoli:")
        lbl9 = QLabel("Mitoses:")
        lbl10 = QLabel("Class:")
        lbl11 = QLabel("Fill The Details To Check The Class Of Breast Cancer")
        lbl12 = QLabel("INFORMATION")

        btn1 = QPushButton("CHECK CLASS")
        image = QImage(os.path.abspath("img2.jpg"))
        sImage = image.scaled(QSize(1950, 1000))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.edit3 = QLineEdit()
        self.edit4 = QLineEdit()
        self.edit5 = QLineEdit()
        self.edit6 = QLineEdit()
        self.edit7 = QLineEdit()
        self.edit8 = QLineEdit()
        self.edit9 = QLineEdit()
        self.edit10 = QLineEdit()
        self.edit11 = QLineEdit()
        self.edit12 = QLineEdit()



        btn1.setFont(newfont)
        lbl1.setFont(newfont)
        lbl2.setFont(newfont)
        lbl3.setFont(newfont)
        lbl4.setFont(newfont)
        lbl5.setFont(newfont)
        lbl6.setFont(newfont)
        lbl7.setFont(newfont)
        lbl8.setFont(newfont)
        lbl9.setFont(newfont)
        lbl10.setFont(newfont)
        lbl11.setFont(newfont1)
        self.edit1.setFont(newfont)
        self.edit2.setFont(newfont)
        self.edit3.setFont(newfont)
        self.edit4.setFont(newfont)
        self.edit5.setFont(newfont)
        self.edit6.setFont(newfont)
        self.edit7.setFont(newfont)
        self.edit8.setFont(newfont)
        self.edit9.setFont(newfont)
        self.edit10.setFont(newfont)
        self.edit11.setFont(newfont2)
        self.edit12.setFont(newfont2)

        grid = QGridLayout()
        grid.setSpacing(5)
        grid.addWidget(lbl1, 1, 0)
        grid.addWidget(lbl2, 1, 3, 1, 1)
        grid.addWidget(lbl3, 2, 0)
        grid.addWidget(lbl4, 2, 3, 1, 1)
        grid.addWidget(lbl5, 3, 0)
        grid.addWidget(lbl6, 3, 3, 1, 1)
        grid.addWidget(lbl7, 4, 0)
        grid.addWidget(lbl8, 4, 3, 1, 1)
        grid.addWidget(lbl9, 5, 0, 1, 1)
        grid.addWidget(lbl10, 9, 0,1,1)
        grid.addWidget(btn1, 7, 1, 1, 3)
        grid.addWidget(self.edit1, 1, 1, 1, 1)
        grid.addWidget(self.edit2, 1, 4, 1, 1)
        grid.addWidget(self.edit3, 2, 1, 1, 1)
        grid.addWidget(self.edit4, 2, 4, 1, 1)
        grid.addWidget(self.edit5, 3, 1, 1, 1)
        grid.addWidget(self.edit6, 3, 4, 1, 1)
        grid.addWidget(self.edit7, 4, 1, 1, 1)
        grid.addWidget(self.edit8, 4, 4, 1, 1)
        grid.addWidget(self.edit9, 5, 1, 1, 1)
        grid.addWidget(self.edit10, 9, 1, 1, 1)
        grid.addWidget(self.edit11, 11, 0, 1, 6)
        grid.addWidget(self.edit12, 12, 0, 1, 6)

        btn1.clicked.connect(self.test)

        self.setLayout(grid)
        self.show()

    def test(self):
        try:
            a = self.edit1.text()
            b = self.edit2.text()
            c = self.edit3.text()
            d = self.edit4.text()
            e = self.edit5.text()
            f = self.edit6.text()
            g = self.edit7.text()
            h = self.edit8.text()
            i = self.edit9.text()

            result = " "
            allvalid = True
            #print("hello1")

            if isEmpty(a):
                result += "Please Fill some number in clump_thickness Box\n\n"
                allvalid = False
            elif not isNumber(a):
                result += "Please Fill number in clump_thickness Box\n\n"
                allvalid = False
            if isEmpty(b):
                result += "Please Fill some number in uniform_cell_size Box\n\n"
                allvalid = False
            elif not isNumber(b):
                result += "Please Fill number in uniform_cell_size Box\n\n"
                allvalid = False
            if isEmpty(c):
                result += "Please Fill some number in uniform_cell_shape Box\n\n"
                allvalid = False
            elif not isNumber(c):
                result += "Please Fill number in uniform_cell_shape Box\n\n"
                allvalid = False
            if isEmpty(d):
                result += "Please Fill some number in marginal_adhesion Box\n\n"
                allvalid = False
            elif not isNumber(d):
                result += "Please Fill number in marginal_adhesion Box\n\n"
                allvalid = False
            if isEmpty(e):
                result += "Please Fill some number in single_epithelial_size Box\n\n"
                allvalid = False
            elif not isNumber(e):
                result += "Please Fill number in single_epithelial_size Box\n\n"
                allvalid = False
            if isEmpty(f):
                result += "Please Fill some number in bare_nuclei Box\n\n"
                allvalid = False
            elif not isNumber(f):
                result += "Please Fill number in bare_nuclei Box\n\n"
                allvalid = False
            if isEmpty(g):
                result += "Please Fill some number in bland_chromatin Box\n\n"
                allvalid = False
            elif not isNumber(g):
                result += "Please Fill number in bland_chromatin Box\n\n"
                allvalid = False
            if isEmpty(h):
                result += "Please Fill some number in normal_nucleoli Box\n\n"
                allvalid = False
            elif not isNumber(h):
                result += "Please Fill number in normal_nucleoli Box\n\n"
                allvalid = False
            if isEmpty(i):
                result += "Please Fill some number in mitoses Box\n\n"
                allvalid = False
            if not isNumber(i):
                result += "Please Fill number in mitoses Box\n\n"
                allvalid = False

            if allvalid == True:
                try:
                    testlist=[]
                    testlist.append(a)
                    testlist.append(b)
                    testlist.append(c)
                    testlist.append(d)
                    testlist.append(e)
                    testlist.append(f)
                    testlist.append(g)
                    testlist.append(h)
                    testlist.append(i)
                    testlist1=[]
                    testlist1.append(testlist)

                    nam = ['id', 'clump_thickness', 'uniform_cell_size', 'uniform_cell_shape',
                           'marginal_adhesion', 'single_epithelial_size', 'bare_nuclei',
                           'bland_chromatin', 'normal_nucleoli', 'mitoses', 'class']
                    self.data = pd.read_csv("C:\\Users\\Spyx\\Documents\\Arduino\\Breast_Cancer_Detection-Used-PYQT5-for-GUI--master\\Breast_Cancer_Detection-Used-PYQT5-for-GUI--master\\dataset\\breast_cancer.csv", names=nam)
                    # data=pd.read_csv(url,names=nam)
                    self.data = self.data.replace('?', '-999')
                    self.y = self.data["class"]
                    self.x = self.data.drop('class', axis=1)
                    self.x = self.x.drop('id', axis=1)
                    self.xtrain, self.xtest, self.ytrain, self.ytest = train_test_split(self.x, self.y, test_size=0.1,
                                                                                        random_state=10)
                    from sklearn.linear_model import LogisticRegression
                    self.clf1 = LogisticRegression()
                    self.clf1.fit(self.xtrain, self.ytrain)

                    testlist2 = pd.DataFrame(testlist1)
                    ypred = self.clf1.predict(testlist2)
                    if ypred[0]==2:
                        stage="benign"
                    else:
                        stage="malignant"


                    self.accpred=self.clf1.predict(self.xtest)
                    predacc = accuracy_score(self.accpred, self.ytest)

                    self.edit10.setText(stage)
                    countb = 0
                    countm = 0
                    mylist = self.data['class']
                    for x in mylist:
                        if x == 2:
                            countb += 1
                        else:
                            countm += 1
                    countb = (countb / 699) * 100
                    countm = (countm / 699) * 100
                    msg1= 'benign is a curable cancer and it has positive result count of ' + str(countb)
                    msg2= 'malignant is a non-curable cancer and it has positive result count of ' + str(countm)
                    self.edit11.setText(msg1)
                    self.edit12.setText(msg2)
                    result = "   SUCCESS  "

                except BaseException as ex:
                    print(ex)
            showMessageDialog(self, result)
        except BaseException as ex:
            print(ex)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = cancdet()
    sys.exit(app.exec_())
