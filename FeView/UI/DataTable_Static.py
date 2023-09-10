# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataTable_Static.ui'
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
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(828, 553)
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget_static = QTableWidget(MainWindow)
        if (self.tableWidget_static.columnCount() < 16):
            self.tableWidget_static.setColumnCount(16)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_static.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_static.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_static.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_static.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_static.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_static.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_static.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_static.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_static.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_static.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_static.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_static.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_static.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_static.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_static.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_static.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        self.tableWidget_static.setObjectName(u"tableWidget_static")
        self.tableWidget_static.setStyleSheet(u"QHeaderView::section {background-color:green}")
        self.tableWidget_static.setAlternatingRowColors(True)
        self.tableWidget_static.setGridStyle(Qt.DashLine)
        self.tableWidget_static.horizontalHeader().setCascadingSectionResizes(False)

        self.gridLayout.addWidget(self.tableWidget_static, 0, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(MainWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)

        self.btn_save_data_static = QPushButton(MainWindow)
        self.btn_save_data_static.setObjectName(u"btn_save_data_static")

        self.gridLayout.addWidget(self.btn_save_data_static, 1, 1, 1, 1)


        self.retranslateUi(MainWindow)
        self.buttonBox.accepted.connect(MainWindow.accept)
        self.buttonBox.rejected.connect(MainWindow.reject)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Static Analysis", None))
        ___qtablewidgetitem = self.tableWidget_static.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Node ID", None));
        ___qtablewidgetitem1 = self.tableWidget_static.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem2 = self.tableWidget_static.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Y", None));
        ___qtablewidgetitem3 = self.tableWidget_static.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Z", None));
        ___qtablewidgetitem4 = self.tableWidget_static.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Ux", None));
        ___qtablewidgetitem5 = self.tableWidget_static.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Uy", None));
        ___qtablewidgetitem6 = self.tableWidget_static.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Uz", None));
        ___qtablewidgetitem7 = self.tableWidget_static.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Rx", None));
        ___qtablewidgetitem8 = self.tableWidget_static.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Ry", None));
        ___qtablewidgetitem9 = self.tableWidget_static.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Rz", None));
        ___qtablewidgetitem10 = self.tableWidget_static.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"RFx", None));
        ___qtablewidgetitem11 = self.tableWidget_static.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"RFy", None));
        ___qtablewidgetitem12 = self.tableWidget_static.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"RFz", None));
        ___qtablewidgetitem13 = self.tableWidget_static.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"RMx", None));
        ___qtablewidgetitem14 = self.tableWidget_static.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"RMy", None));
        ___qtablewidgetitem15 = self.tableWidget_static.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"RMz", None));
        self.btn_save_data_static.setText(QCoreApplication.translate("MainWindow", u"Save Data as Excell", None))
    # retranslateUi

