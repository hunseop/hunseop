# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import bcrypt
    
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(349, 97)
        Dialog.setMinimumSize(QtCore.QSize(349, 97))
        Dialog.setMaximumSize(QtCore.QSize(349, 97))
        Dialog.setStyleSheet("background-color: rgb(95, 95, 95);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_password = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_password.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setPlaceholderText("Please enter password")
        self.horizontalLayout.addWidget(self.lineEdit_password)
        self.pushButton_enter = QtWidgets.QPushButton(Dialog)
        self.pushButton_enter.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_enter.setObjectName("pushButton_enter")
        self.horizontalLayout.addWidget(self.pushButton_enter)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.pushButton_enter.clicked.connect(self.login)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def login(self):
        key = "dnRlwlak3!"
        pw = self.lineEdit_password.text()
        hashed_pw = bcrypt.hashpw(password=pw.encode('utf-8'), salt=bcrypt.gensalt()) 
        print(hashed_pw)

        if bcrypt.checkpw(key.encode('utf-8'), hashed_pw):
            print("로그인 성공")

        else:
            print("로그인 실패")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "Password"))
        self.pushButton_enter.setText(_translate("Dialog", "Enter"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())