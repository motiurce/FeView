# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoadSetting.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(265, 151)
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(MainWindow)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label = QLabel(MainWindow)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.cb_ls_font_color = QComboBox(MainWindow)
        self.cb_ls_font_color.addItem("")
        self.cb_ls_font_color.addItem("")
        self.cb_ls_font_color.addItem("")
        self.cb_ls_font_color.addItem("")
        self.cb_ls_font_color.addItem("")
        self.cb_ls_font_color.addItem("")
        self.cb_ls_font_color.addItem("")
        self.cb_ls_font_color.addItem("")
        self.cb_ls_font_color.setObjectName(u"cb_ls_font_color")

        self.gridLayout.addWidget(self.cb_ls_font_color, 4, 2, 1, 1)

        self.label_2 = QLabel(MainWindow)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.tb_ls_arrow_size = QLineEdit(MainWindow)
        self.tb_ls_arrow_size.setObjectName(u"tb_ls_arrow_size")
        self.tb_ls_arrow_size.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.tb_ls_arrow_size, 0, 2, 1, 1)

        self.tb_ls_font_size = QLineEdit(MainWindow)
        self.tb_ls_font_size.setObjectName(u"tb_ls_font_size")
        self.tb_ls_font_size.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.tb_ls_font_size, 3, 2, 1, 1)

        self.label_4 = QLabel(MainWindow)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(MainWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 6, 2, 1, 1)

        self.cb_ls_arrow_color = QComboBox(MainWindow)
        self.cb_ls_arrow_color.addItem("")
        self.cb_ls_arrow_color.addItem("")
        self.cb_ls_arrow_color.addItem("")
        self.cb_ls_arrow_color.addItem("")
        self.cb_ls_arrow_color.addItem("")
        self.cb_ls_arrow_color.addItem("")
        self.cb_ls_arrow_color.addItem("")
        self.cb_ls_arrow_color.addItem("")
        self.cb_ls_arrow_color.setObjectName(u"cb_ls_arrow_color")

        self.gridLayout.addWidget(self.cb_ls_arrow_color, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 2, 1, 1)


        self.retranslateUi(MainWindow)
        self.buttonBox.accepted.connect(MainWindow.accept)
        self.buttonBox.rejected.connect(MainWindow.reject)

        self.cb_ls_font_color.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Arrow Size", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Load Values Size", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Arrows Size : ", None))
        self.cb_ls_font_color.setItemText(0, QCoreApplication.translate("MainWindow", u"Red", None))
        self.cb_ls_font_color.setItemText(1, QCoreApplication.translate("MainWindow", u"Green", None))
        self.cb_ls_font_color.setItemText(2, QCoreApplication.translate("MainWindow", u"Blue", None))
        self.cb_ls_font_color.setItemText(3, QCoreApplication.translate("MainWindow", u"Cyan", None))
        self.cb_ls_font_color.setItemText(4, QCoreApplication.translate("MainWindow", u"Magenta", None))
        self.cb_ls_font_color.setItemText(5, QCoreApplication.translate("MainWindow", u"Yellow", None))
        self.cb_ls_font_color.setItemText(6, QCoreApplication.translate("MainWindow", u"Black", None))
        self.cb_ls_font_color.setItemText(7, QCoreApplication.translate("MainWindow", u"White", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Arrows Color : ", None))
        self.tb_ls_arrow_size.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.tb_ls_font_size.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Load Values Color", None))
        self.cb_ls_arrow_color.setItemText(0, QCoreApplication.translate("MainWindow", u"Red", None))
        self.cb_ls_arrow_color.setItemText(1, QCoreApplication.translate("MainWindow", u"Green", None))
        self.cb_ls_arrow_color.setItemText(2, QCoreApplication.translate("MainWindow", u"Blue", None))
        self.cb_ls_arrow_color.setItemText(3, QCoreApplication.translate("MainWindow", u"Cyan", None))
        self.cb_ls_arrow_color.setItemText(4, QCoreApplication.translate("MainWindow", u"Magenta", None))
        self.cb_ls_arrow_color.setItemText(5, QCoreApplication.translate("MainWindow", u"Yellow", None))
        self.cb_ls_arrow_color.setItemText(6, QCoreApplication.translate("MainWindow", u"Black", None))
        self.cb_ls_arrow_color.setItemText(7, QCoreApplication.translate("MainWindow", u"White", None))

    # retranslateUi

