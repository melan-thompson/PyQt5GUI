from PyQt5.QtWidgets import QWidget

from inputWidgets.InputBaseWidget import InputBaseWidget


class CylinderInputWidget(InputBaseWidget):
    def __init__(self):
        InputBaseWidget.__init__(self)
        self.addParameter('气缸直径', ['mm'])
        self.addParameter('冲程', ['mm'])
        self.addParameter('曲柄连杆比', [''])
        self.addParameter('压缩比', [''])
        self.addParameter('气缸数', [''])
        self.addParameter('发火顺序', [''])