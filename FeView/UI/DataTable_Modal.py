# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataTable_Modal.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractScrollArea, QApplication, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QHeaderView,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(519, 337)
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(MainWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 1)

        self.btn_save_data_modal = QPushButton(MainWindow)
        self.btn_save_data_modal.setObjectName(u"btn_save_data_modal")

        self.gridLayout.addWidget(self.btn_save_data_modal, 2, 1, 1, 1)

        self.tableWidget_Modal = QTableWidget(MainWindow)
        if (self.tableWidget_Modal.columnCount() < 4):
            self.tableWidget_Modal.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_Modal.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_Modal.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_Modal.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_Modal.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_Modal.setObjectName(u"tableWidget_Modal")
        self.tableWidget_Modal.setAutoFillBackground(False)
        self.tableWidget_Modal.setStyleSheet(u"QHeaderView::section {background-color:green}")
        self.tableWidget_Modal.setFrameShape(QFrame.Box)
        self.tableWidget_Modal.setFrameShadow(QFrame.Sunken)
        self.tableWidget_Modal.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_Modal.setDragEnabled(False)
        self.tableWidget_Modal.setAlternatingRowColors(True)
        self.tableWidget_Modal.setTextElideMode(Qt.ElideRight)
        self.tableWidget_Modal.setGridStyle(Qt.DashLine)
        self.tableWidget_Modal.setSortingEnabled(False)
        self.tableWidget_Modal.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Modal.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_Modal.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_Modal.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_Modal.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_Modal.verticalHeader().setVisible(False)
        self.tableWidget_Modal.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Modal.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_Modal.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.tableWidget_Modal, 1, 1, 1, 1)


        self.retranslateUi(MainWindow)
        self.buttonBox.accepted.connect(MainWindow.accept)
        self.buttonBox.rejected.connect(MainWindow.reject)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Modal Analysis", None))
        self.btn_save_data_modal.setText(QCoreApplication.translate("MainWindow", u"Save Data as Excell", None))
        ___qtablewidgetitem = self.tableWidget_Modal.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Mode Number", None));
        ___qtablewidgetitem1 = self.tableWidget_Modal.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Period (sec)", None));
        ___qtablewidgetitem2 = self.tableWidget_Modal.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Frequency (Hz)", None));
        ___qtablewidgetitem3 = self.tableWidget_Modal.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Frequency (Rad/sec)", None));
    # retranslateUi

