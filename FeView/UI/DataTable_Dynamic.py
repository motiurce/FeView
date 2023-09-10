# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataTable_Dynamic.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QHeaderView, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(828, 564)
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(MainWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)

        self.tabWidget = QTabWidget(MainWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget_dynamic_disp = QTableWidget(self.tab)
        self.tableWidget_dynamic_disp.setObjectName(u"tableWidget_dynamic_disp")
        self.tableWidget_dynamic_disp.setStyleSheet(u"QHeaderView::section {background-color:green}")
        self.tableWidget_dynamic_disp.setAlternatingRowColors(True)
        self.tableWidget_dynamic_disp.setGridStyle(Qt.DashLine)
        self.tableWidget_dynamic_disp.horizontalHeader().setCascadingSectionResizes(False)

        self.gridLayout_2.addWidget(self.tableWidget_dynamic_disp, 0, 0, 1, 1)

        self.btn_save_data_static = QPushButton(self.tab)
        self.btn_save_data_static.setObjectName(u"btn_save_data_static")

        self.gridLayout_2.addWidget(self.btn_save_data_static, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)


        self.retranslateUi(MainWindow)
        self.buttonBox.accepted.connect(MainWindow.accept)
        self.buttonBox.rejected.connect(MainWindow.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dynamic Analysis", None))
        self.btn_save_data_static.setText(QCoreApplication.translate("MainWindow", u"Save Data as Excell", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Displacement", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Rotation", None))
    # retranslateUi

