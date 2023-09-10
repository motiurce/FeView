# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
    QFrame, QGridLayout, QLabel, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(443, 261)
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(MainWindow)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 2)

        self.line = QFrame(MainWindow)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)

        self.line_2 = QFrame(MainWindow)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 7, 0, 1, 2)

        self.label_3 = QLabel(MainWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 2)

        self.label_4 = QLabel(MainWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 2)

        self.buttonBox = QDialogButtonBox(MainWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 9, 1, 1, 1)

        self.label_7 = QLabel(MainWindow)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(80, 80))
        self.label_7.setMaximumSize(QSize(80, 80))
        self.label_7.setPixmap(QPixmap(u"icon/FeView_ico.ico"))
        self.label_7.setScaledContents(True)

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 8, 1, 1, 1)

        self.label = QLabel(MainWindow)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(48)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_6 = QLabel(MainWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 2)

        self.label_2 = QLabel(MainWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)


        self.retranslateUi(MainWindow)
        self.buttonBox.accepted.connect(MainWindow.accept)
        self.buttonBox.rejected.connect(MainWindow.reject)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"About FeView", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Department of Civil Engineering, Kunsan National University", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version: 1.0 (Beta) ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Copyright Structural System Laboratory @ 2020", None))
        self.label_7.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"FeView", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Developed By: Md Motiur Rahman, Tahmina Tasnim Nahar, Dookie kim", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"FeView: Finite Element Model Visualization for OpenSees", None))
    # retranslateUi

