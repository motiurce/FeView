# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ResponseWindows.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QGridLayout,
    QGroupBox, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(873, 347)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(150, 0))
        self.groupBox.setMaximumSize(QSize(150, 16777215))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.cb_resp_component = QComboBox(self.groupBox)
        self.cb_resp_component.addItem("")
        self.cb_resp_component.addItem("")
        self.cb_resp_component.addItem("")
        self.cb_resp_component.addItem("")
        self.cb_resp_component.addItem("")
        self.cb_resp_component.addItem("")
        self.cb_resp_component.addItem("")
        self.cb_resp_component.addItem("")
        self.cb_resp_component.addItem("")
        self.cb_resp_component.addItem("")
        self.cb_resp_component.addItem("")
        self.cb_resp_component.addItem("")
        self.cb_resp_component.addItem("")
        self.cb_resp_component.addItem("")
        self.cb_resp_component.addItem("")
        self.cb_resp_component.addItem("")
        self.cb_resp_component.addItem("")
        self.cb_resp_component.addItem("")
        self.cb_resp_component.setObjectName(u"cb_resp_component")

        self.gridLayout_2.addWidget(self.cb_resp_component, 2, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.cb_resp_nodenumber = QComboBox(self.groupBox)
        self.cb_resp_nodenumber.setObjectName(u"cb_resp_nodenumber")

        self.gridLayout_2.addWidget(self.cb_resp_nodenumber, 1, 1, 1, 1)

        self.apply_repnse = QPushButton(self.groupBox)
        self.apply_repnse.setObjectName(u"apply_repnse")

        self.gridLayout_2.addWidget(self.apply_repnse, 3, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.rbtn_sesp_static = QRadioButton(self.groupBox_3)
        self.rbtn_sesp_static.setObjectName(u"rbtn_sesp_static")
        self.rbtn_sesp_static.setChecked(True)

        self.gridLayout_4.addWidget(self.rbtn_sesp_static, 0, 0, 1, 1)

        self.rbtn_sesp_dynamic = QRadioButton(self.groupBox_3)
        self.rbtn_sesp_dynamic.setObjectName(u"rbtn_sesp_dynamic")

        self.gridLayout_4.addWidget(self.rbtn_sesp_dynamic, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_3, 0, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.plt_response = QGraphicsView(self.groupBox_2)
        self.plt_response.setObjectName(u"plt_response")

        self.gridLayout_3.addWidget(self.plt_response, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 873, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Reponse Plot", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Component", None))
        self.cb_resp_component.setItemText(0, QCoreApplication.translate("MainWindow", u"Ux", None))
        self.cb_resp_component.setItemText(1, QCoreApplication.translate("MainWindow", u"Uy", None))
        self.cb_resp_component.setItemText(2, QCoreApplication.translate("MainWindow", u"Uz", None))
        self.cb_resp_component.setItemText(3, QCoreApplication.translate("MainWindow", u"Rx", None))
        self.cb_resp_component.setItemText(4, QCoreApplication.translate("MainWindow", u"Ry", None))
        self.cb_resp_component.setItemText(5, QCoreApplication.translate("MainWindow", u"Rz", None))
        self.cb_resp_component.setItemText(6, QCoreApplication.translate("MainWindow", u"RFx", None))
        self.cb_resp_component.setItemText(7, QCoreApplication.translate("MainWindow", u"RFy", None))
        self.cb_resp_component.setItemText(8, QCoreApplication.translate("MainWindow", u"RFz", None))
        self.cb_resp_component.setItemText(9, QCoreApplication.translate("MainWindow", u"RMx", None))
        self.cb_resp_component.setItemText(10, QCoreApplication.translate("MainWindow", u"RMy", None))
        self.cb_resp_component.setItemText(11, QCoreApplication.translate("MainWindow", u"RMz", None))
        self.cb_resp_component.setItemText(12, QCoreApplication.translate("MainWindow", u"Ax", None))
        self.cb_resp_component.setItemText(13, QCoreApplication.translate("MainWindow", u"Ay", None))
        self.cb_resp_component.setItemText(14, QCoreApplication.translate("MainWindow", u"Az", None))
        self.cb_resp_component.setItemText(15, QCoreApplication.translate("MainWindow", u"Vx", None))
        self.cb_resp_component.setItemText(16, QCoreApplication.translate("MainWindow", u"Vy", None))
        self.cb_resp_component.setItemText(17, QCoreApplication.translate("MainWindow", u"Vz", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Node Number", None))
        self.apply_repnse.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Analysis Type", None))
        self.rbtn_sesp_static.setText(QCoreApplication.translate("MainWindow", u"Satatic", None))
        self.rbtn_sesp_dynamic.setText(QCoreApplication.translate("MainWindow", u"Transient", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Response Plot", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

