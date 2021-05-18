import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene

matplotlib.use("Qt5Agg")  # 声明使用QT5

class MyFigureCanvas(FigureCanvasQTAgg):
    '''
    通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplotlib的关键
    '''

    def __init__(self, parent=None, width=10, height=5, xlim=(0, 200), ylim=(-2, 2), dpi=100):
        # 创建一个Figure
        fig = plt.Figure(figsize=(width, height), dpi=dpi, tight_layout=True)  # tight_layout: 用于去除画图时两边的空白

        FigureCanvasQTAgg.__init__(self, fig)  # 初始化父类
        self.setParent(parent)

        self.axes = fig.add_subplot(111)  # 添加子图
        self.axes.spines['top'].set_visible(False)  # 去掉绘图时上面的横线
        self.axes.spines['right'].set_visible(False)  # 去掉绘图时右面的横线
        self.axes.set_xlim(xlim)
        self.axes.set_ylim(ylim)

class CanvasView(QGraphicsView):
    def __init__(self):
        QGraphicsView.__init__(self)
        self.gv_visual_data_content = MyFigureCanvas(width=self.width() / 101,
                                                     height=self.height() / 101,
                                                     xlim=(0, 2 * np.pi),
                                                     ylim=(-1, 1))
        x = np.arange(0, 2 * np.pi, np.pi / 100)
        y = np.cos(x)
        self.gv_visual_data_content.axes.plot(x, y)
        self.gv_visual_data_content.axes.set_title('cos()')
        # 加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        self.graphic_scene = QGraphicsScene()  # 创建一个QGraphicsScene
        self.graphic_scene.addWidget(
            self.gv_visual_data_content)  # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
        self.setScene(self.graphic_scene)  # 把QGraphicsScene放入QGraphicsView
        ##########################################################
        # x = np.arange(0, 2 * np.pi, np.pi / 100)
        # y = np.sin(x)
        # self.gv_visual_data_content.axes.clear()  # 由于图片需要反复绘制，所以每次绘制前清空，然后绘图
        # self.gv_visual_data_content.axes.plot(x, y)
        # self.gv_visual_data_content.axes.set_title('sin()')
        # self.gv_visual_data_content.draw()
        ##########################################################
        self.show()
