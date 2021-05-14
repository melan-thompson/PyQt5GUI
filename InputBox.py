from PyQt5.QtWidgets import QWidget,QLabel,QLineEdit,QComboBox,QHBoxLayout,QSizePolicy
from PyQt5.QtGui import QFont

class InputBox(QWidget):
    def __init__(self,parent=None,paraname="Emptyname"):
        Font = QFont()
        Font.setPointSize(20)

        super(QWidget,self).__init__(parent)
        layout=QHBoxLayout()
        label=QLabel(self)
        label.resize(100,50)
        label.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Preferred))
        label.setText(paraname)
        label.setFont(Font)
        layout.addWidget(label)

        edit=QLineEdit(self)
        edit.setFont(Font)
        layout.addWidget(edit)

        combox=QComboBox(self)
        combox.setFont(Font)
        layout.addWidget(combox)

        self.setFixedHeight(50)

        self.setLayout(layout)