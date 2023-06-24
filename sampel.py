from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("index calculator")
        Form.resize(304, 123)
        Form.setStyleSheet("background-color:qlineargradient(spread:repeat, x1:0, y1:0.00568182, x2:1, y2:1, stop:0.157635 rgba(37, 91, 40, 255), stop:1 rgba(255, 255, 255, 255))")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 113, 21))
        self.lineEdit.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0.157635 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255))")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 30, 113, 21))
        self.lineEdit_2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0.157635 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255))")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 90, 16))
        self.label.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0.157635 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255))")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 90, 16))
        self.label_2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0.157635 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255))")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 80, 241, 32))
        self.pushButton.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0.157635 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255))")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 161, 16))
        self.label_3.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0.157635 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255))")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Body mass index calculator"))
        self.label.setText(_translate("Form", "Weight/kg"))
        self.label_2.setText(_translate("Form", "Growth/cm"))
        self.pushButton.setText(_translate("Form", "Calculate"))
        self.label_3.setText(_translate("Form", "Your mass index: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
