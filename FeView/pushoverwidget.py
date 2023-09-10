from PySide6.QtWidgets import *
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
class PushoverWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.fig_pushover = Figure()
        self.fig_pushover.set_facecolor('#ffffff')
        self.canvas_pushover = FigureCanvas(self.fig_pushover)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas_pushover)
        self.canvas_pushover.axes_pushover = self.canvas_pushover.figure.add_subplot(111)
        self.setLayout(vertical_layout)

        self.canvas_pushover.axes_pushover.set_xticks([])
        self.canvas_pushover.axes_pushover.set_yticks([])
        self.canvas_pushover.axes_pushover.axis('off')
        self.fig_pushover.subplots_adjust(left=0.10, bottom=0.15, right=0.985, top=0.95)
        self.toolbar = NavigationToolbar(self.canvas_pushover, self)
        self.toolbar.setFixedHeight(25)
        vertical_layout.addWidget(self.toolbar)