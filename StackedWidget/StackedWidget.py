from PyQt5.QtWidgets import QStackedWidget

from Utility.Utility import WidgetType
from inputWidgets.CylinderInputWidget import CylinderInputWidget


class StackedWidget(QStackedWidget):
    WidgetDic = {}

    # def __init__(self):
    #     QStackedWidget.__init__(self)
    #     cylinderWidget = CylinderWidget()
    #     self.WidgetDic[WidgetType.Cylinder] = cylinderWidget
    #     self.addWidget(cylinderWidget)
    #
    # def componentWidgetSwitch(self, widgetType):
    #     componentWidget = self.WidgetDic[WidgetType.Cylinder]
    #     self.setCurrentWidget(componentWidget)