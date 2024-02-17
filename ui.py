from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 598)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(300, 10, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text.setFont(font)
        self.text.setObjectName("text")
        self.resuld = QtWidgets.QLabel(self.centralwidget)
        self.resuld.setGeometry(QtCore.QRect(310, 70, 111, 41))
        self.resuld.setObjectName("resuld")
        self.cheknun = QtWidgets.QCheckBox(self.centralwidget)
        self.cheknun.setGeometry(QtCore.QRect(290, 110, 191, 41))
        self.cheknun.setObjectName("cheknun")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(290, 140, 201, 71))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 210, 121, 31))
        self.pushButton.setStyleSheet("border:2px seld green;\n"
"border-rabius:10px;\n"
"background-color:purple;\n"
"color:green;\n"
"padding:5px;")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Вікно пароль"))
        self.text.setText(_translate("MainWindow", "Генератор паролів"))
        self.resuld.setText(_translate("MainWindow", "Тут буде результат"))
        self.cheknun.setText(_translate("MainWindow", "Використовувати числа"))
        self.checkBox_2.setText(_translate("MainWindow", "Використовувати алфавіт"))
        self.pushButton.setText(_translate("MainWindow", "Згенерувати"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
