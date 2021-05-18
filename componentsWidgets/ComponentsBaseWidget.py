from PyQt5.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout

from Utility.Utility import WidgetType
from inputWidgets.CylinderInputWidget import CylinderInputWidget
from inputWidgets.InputBaseWidget import InputBaseWidget


class ComponentsBaseWidget(QWidget):
    treeWidget = QTreeWidget
    vboxLayout = QVBoxLayout

    def __init__(self):
        QWidget.__init__(self)
        self.vboxLayout = QVBoxLayout()
        self.setLayout(self.vboxLayout)
        # self.treeWidget = QTreeWidget()
        # self.treeWidget.setColumnCount(1)
        # self.treeWidget.setHeaderHidden(True)
        # ##############################################
        # treeList = []
        # # QTreeWidgetItem(self.treeWidget, ['top'])
        # # QTreeWidgetItem(self.treeWidget, ['top2'])
        # TreeWidgetItem(WidgetType.Cylinder, self.treeWidget, ['top2'])
        # # for num in range(0, 10):
        # #     treeWidgetItem.insertChild()
        # #     # treeList.append(treeWidgetItem)
        # ##############################################
        # # self.treeWidget.addTopLevelItems(treeList)
        #
        # vboxLayout = QVBoxLayout()
        # vboxLayout.addWidget(self.treeWidget)
        # self.setLayout(vboxLayout)


class TreeWidgetItem(QTreeWidgetItem):
    # QTreeWidgetItem(QTreeWidget, Iterable[str], type: int = QTreeWidgetItem.Type)
    widgetType = WidgetType

    def __init__(self, widgetType, *__args):
        QTreeWidgetItem.__init__(self, *__args)
        self.widgetType = widgetType

