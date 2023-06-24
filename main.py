import PyQt5
import sys
from operator import truediv
from PyQt5 import QtWidgets
from sampel import Ui_Form

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()


def addiation():
    try:
        x = ui.lineEdit.text()
        y = ui.lineEdit_2.text()
        y_copy = int(y) / 100
        z = str(truediv(int(x), y_copy ** 2))
        ui.label_3.setText(f'Your mass index: {z}')
    except ValueError:
        ui.label_3.setText('Error')

ui.pushButton.clicked.connect(addiation)

sys.exit(app.exec_())
