from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem

from Utility.Utility import WidgetType


class ComponentsTreeWidget(QTreeWidget):
    def __init__(self):
        QTreeWidget.__init__(self)
        ComponentTreeItem(self.treeWidget, WidgetType.Cylinder, ['气缸'])


class ComponentTreeItem(QTreeWidgetItem):
    type = WidgetType

    def __init__(self, widgettype, *__args):
        QTreeWidgetItem.__init__(self, *__args)
        self.type = widgettype
