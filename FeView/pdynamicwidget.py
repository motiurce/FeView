from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
class PdynamicWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.fig_pdynamic = Figure()
        self.fig_pdynamic.set_facecolor('#ffffff')
        self.canvas_pdynamic = FigureCanvas(self.fig_pdynamic)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas_pdynamic)
        self.canvas_pdynamic.axes_pdynamic = self.canvas_pdynamic.figure.add_subplot(111)
        self.setLayout(vertical_layout)

        self.canvas_pdynamic.axes_pdynamic.set_xticks([])
        self.canvas_pdynamic.axes_pdynamic.set_yticks([])
        self.canvas_pdynamic.axes_pdynamic.axis('off')
        self.fig_pdynamic.subplots_adjust(left=0.12, bottom=0.15, right=0.985, top=0.95)
        self.toolbar = NavigationToolbar(self.canvas_pdynamic, self)
        self.toolbar.setFixedHeight(25)
        vertical_layout.addWidget(self.toolbar)