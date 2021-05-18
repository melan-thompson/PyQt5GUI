from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QComboBox


class InputBaseWidget(QWidget):
    vboxLayout = QVBoxLayout

    def __init__(self):
        QWidget.__init__(self)
        self.vboxLayout = QVBoxLayout()
        self.setLayout(self.vboxLayout)

    def addParameter(self, parameter, units):
        hboxLayout = QHBoxLayout()
        label = QLabel(parameter)
        lineEdit = QLineEdit()
        comboBox = QComboBox()
        comboBox.addItems(units)
        hboxLayout.addWidget(label)
        hboxLayout.addWidget(lineEdit)
        hboxLayout.addWidget(comboBox)
        self.vboxLayout.addLayout(hboxLayout)

