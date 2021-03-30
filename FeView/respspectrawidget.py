from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
class RespspectraWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.fig_rs = Figure()
        self.fig_rs.set_facecolor('#ffffff')
        self.canvas_rs = FigureCanvas(self.fig_rs)
        vertical_layout = QHBoxLayout()
        vertical_layout.addWidget(self.canvas_rs)
        self.canvas_rs.axes_rs = self.canvas_rs.figure.add_subplot(111)
        self.setLayout(vertical_layout)
        self.canvas_rs.axes_rs.set_xticks([])
        self.canvas_rs.axes_rs.set_yticks([])
        self.canvas_rs.axes_rs.axis('off')
        self.fig_rs.subplots_adjust(left=0.12, bottom=0.15, right=0.985, top=0.95)
        self.toolbar = NavigationToolbar(self.canvas_rs, self)
        self.toolbar.setFixedWidth(25)
        self.toolbar.setOrientation(QtCore.Qt.Vertical)
        vertical_layout.addWidget(self.toolbar)