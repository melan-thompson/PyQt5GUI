from PyQt5.QtWidgets import QVBoxLayout, QWidget

from componentsWidgets.ComponentsBaseWidget import ComponentsBaseWidget
from inputWidgets.CylinderInputWidget import CylinderInputWidget


class CylinderWidget(ComponentsBaseWidget):
    cylinderWidget = CylinderInputWidget
    # vboxLayout = QVBoxLayout

    def __init__(self):
        ComponentsBaseWidget.__init__(self)
        self.cylinderWidget = CylinderInputWidget()
        # self.vboxLayout = QVBoxLayout()
        self.vboxLayout.addWidget(self.cylinderWidget)
        widget = QWidget()
        self.vboxLayout.addWidget(widget)
