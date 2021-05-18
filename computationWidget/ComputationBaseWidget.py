from PyQt5.QtWidgets import QVBoxLayout, QWidget, QTabWidget


class ComputationBaseWidget(QWidget):
    tabWidget = QTabWidget
    vboxLayout = QVBoxLayout

    def __init__(self):
        QWidget.__init__(self)
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        vboxLayout = QVBoxLayout(self)
        vboxLayout.addWidget(self.tabWidget)

    def addinputwidget(self, widget):
        self.tabWidget.addTab(widget, '输入')

    def addmodelwidget(self, widget):
        self.tabWidget.addTab(widget, '模型')

    def addoutputwidget(self, widget):
        self.tabWidget.addTab(widget, '输出')
