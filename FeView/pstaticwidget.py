from PySide6.QtWidgets import *
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
class PstaticWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.fig_pstatic = Figure()
        self.fig_pstatic.set_facecolor('#ffffff')
        self.canvas_pstatic = FigureCanvas(self.fig_pstatic)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas_pstatic)
        self.canvas_pstatic.axes_pstatic = self.canvas_pstatic.figure.add_subplot(111)
        self.setLayout(vertical_layout)

        self.canvas_pstatic.axes_pstatic.set_xticks([])
        self.canvas_pstatic.axes_pstatic.set_yticks([])
        self.canvas_pstatic.axes_pstatic.axis('off')
        self.fig_pstatic.subplots_adjust(left=0.12, bottom=0.15, right=0.985, top=0.95)
        self.toolbar = NavigationToolbar(self.canvas_pstatic, self)
        self.toolbar.setFixedHeight(25)
        vertical_layout.addWidget(self.toolbar)