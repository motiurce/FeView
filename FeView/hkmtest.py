# 코드 테스트용 임시파일
import sys
from PySide6 import QtWidgets
from UI.StaticResponseWindows import Ui_MainWindow as hkm
from UI.DynamicResponseWindows import Ui_MainWindow as gphkm
from UI.MainWindows import Ui_MainWindow as mainwindow
from UI.LoadSetting import Ui_MainWindow as loadsetting
from UI.DataTable_Dynamic import Ui_MainWindow as gogogo
class MainWindow(QtWidgets.QMainWindow, gogogo):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()