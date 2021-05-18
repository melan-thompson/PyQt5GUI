from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget

from canvasView.CanvasView import CanvasView
from componentsWidgets.CylinderWidget import CylinderWidget
from computationWidget.ComputationBaseWidget import ComputationBaseWidget


class CylinderComputationWidget(ComputationBaseWidget):
    def __init__(self):
        ComputationBaseWidget.__init__(self)
        widget = QWidget()
        hboxLayout = QHBoxLayout()
        vboxLayout = QVBoxLayout(widget)
        cylinderWidget = CylinderWidget()
        canvasView = CanvasView()
        hboxLayout.addWidget(cylinderWidget)
        hboxLayout.addWidget(canvasView)

        canvasView2 = CanvasView()

        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addWidget(canvasView2)

        self.addinputwidget(widget)
