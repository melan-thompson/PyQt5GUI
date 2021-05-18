import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QAction,QWidget,QLabel,QLineEdit,QComboBox,QHBoxLayout,QGroupBox
# from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from InputBox import InputBox
from componentsWidgets.ComponentsBaseWidget import ComponentsBaseWidget
from componentsWidgets.CylinderWidget import CylinderWidget
from computationWidget.CylinderComputationWidget import CylinderComputationWidget


class Mainwindow(QMainWindow):
    def __init__(self, parent=None):
        super(Mainwindow, self).__init__(parent)

        self.createActions()

        self.cylinderComputationWidget = CylinderComputationWidget()
        self.setCentralWidget(self.cylinderComputationWidget)

        # self.cylinderWidget = CylinderWidget()
        # self.setCentralWidget(self.cylinderWidget)

        # self.componentWidget = ComponentsBaseWidget()
        # self.setCentralWidget(self.componentWidget)

        # Desktop = QApplication.desktop()
        #
        # self.setWindowTitle("Fuel consumption calculation")
        #
        # self.resize(Desktop.width() * 3 // 4, Desktop.height() * 3 // 4)
        #
        # size = self.geometry()
        # self.move((Desktop.width() - size.width()) // 2, (Desktop.height() - size.height()) // 2)
        #
        # self.statusBar().setFixedHeight(50)
        # self.statusBar().showMessage("就绪")
        #
        # menu=self.menuBar()
        # menu.setFixedHeight(30)
        # Font=QFont()
        # Font.setPointSize(12)
        # menu.setFont(Font)
        # file=menu.addMenu("文件")
        # file.addAction("新建")
        # save=QAction("另存为",self)
        # save.setShortcut("Ctrl+s")
        # file.addAction(save)
        # file.addAction(QAction("退出",self))
        #
        # database=menu.addMenu("数据库")
        # database.addAction(QAction("数据库匹配",self))
        # database.addAction((QAction("连接到数据库",self)))
        #
        # layout=QHBoxLayout()
        # Box=InputBox(self,"wod")
        # layout.addWidget(Box)
        # self.setLayout(layout)

    def createActions(self):
        fileMenu = self.menuBar().addMenu('文件')
        dataBaseMenu = self.menuBar().addMenu('数据库')
        helpMenu = self.menuBar().addMenu('获取帮助')

        openFileAction = fileMenu.addAction('打开文件')

        connectDataBaseAction = dataBaseMenu.addAction('连接数据库')






if __name__ == "__main__":
    app = QApplication([])
    form = Mainwindow()
    form.show()
    sys.exit(app.exec())
