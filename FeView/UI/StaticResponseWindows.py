# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StaticResponseWindows.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)

from pstaticwidget import PstaticWidget
from pushoverwidget import PushoverWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(998, 430)
        self.actionSave_Plot = QAction(MainWindow)
        self.actionSave_Plot.setObjectName(u"actionSave_Plot")
        self.actionSave_Data = QAction(MainWindow)
        self.actionSave_Data.setObjectName(u"actionSave_Data")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionChange_Background_Color = QAction(MainWindow)
        self.actionChange_Background_Color.setObjectName(u"actionChange_Background_Color")
        self.actionLine_Style = QAction(MainWindow)
        self.actionLine_Style.setObjectName(u"actionLine_Style")
        self.actionLine_Color = QAction(MainWindow)
        self.actionLine_Color.setObjectName(u"actionLine_Color")
        self.actionLine_Width = QAction(MainWindow)
        self.actionLine_Width.setObjectName(u"actionLine_Width")
        self.actionSolid = QAction(MainWindow)
        self.actionSolid.setObjectName(u"actionSolid")
        self.actionDotted = QAction(MainWindow)
        self.actionDotted.setObjectName(u"actionDotted")
        self.actionDashed = QAction(MainWindow)
        self.actionDashed.setObjectName(u"actionDashed")
        self.actionDashdot = QAction(MainWindow)
        self.actionDashdot.setObjectName(u"actionDashdot")
        self.action0_2 = QAction(MainWindow)
        self.action0_2.setObjectName(u"action0_2")
        self.action0_4 = QAction(MainWindow)
        self.action0_4.setObjectName(u"action0_4")
        self.action0_6 = QAction(MainWindow)
        self.action0_6.setObjectName(u"action0_6")
        self.action0_8 = QAction(MainWindow)
        self.action0_8.setObjectName(u"action0_8")
        self.action1 = QAction(MainWindow)
        self.action1.setObjectName(u"action1")
        self.actionLine_Color_g = QAction(MainWindow)
        self.actionLine_Color_g.setObjectName(u"actionLine_Color_g")
        self.mb_savedata = QAction(MainWindow)
        self.mb_savedata.setObjectName(u"mb_savedata")
        self.actionSave_Pushover_Data = QAction(MainWindow)
        self.actionSave_Pushover_Data.setObjectName(u"actionSave_Pushover_Data")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QHeaderView::section {background-color:green}\n"
"QHeaderView::section {color:white}\n"
"")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_8 = QGridLayout(self.tab_3)
        self.gridLayout_8.setSpacing(2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(2, 0, 2, 2)
        self.groupBox = QGroupBox(self.tab_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(150, 0))
        self.groupBox.setMaximumSize(QSize(200, 16777215))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.cb_dt_static = QCheckBox(self.groupBox)
        self.cb_dt_static.setObjectName(u"cb_dt_static")

        self.gridLayout_2.addWidget(self.cb_dt_static, 6, 0, 1, 1)

        self.gb_sigle_static = QGroupBox(self.groupBox)
        self.gb_sigle_static.setObjectName(u"gb_sigle_static")
        self.gridLayout_4 = QGridLayout(self.gb_sigle_static)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.label = QLabel(self.gb_sigle_static)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)

        self.cb_resp_nodenumber = QComboBox(self.gb_sigle_static)
        self.cb_resp_nodenumber.setObjectName(u"cb_resp_nodenumber")

        self.gridLayout_4.addWidget(self.cb_resp_nodenumber, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.gb_sigle_static, 2, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 7, 2, 1, 1)

        self.tb_dt_static = QLineEdit(self.groupBox)
        self.tb_dt_static.setObjectName(u"tb_dt_static")
        self.tb_dt_static.setEnabled(False)

        self.gridLayout_2.addWidget(self.tb_dt_static, 6, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_6 = QGridLayout(self.groupBox_5)
        self.gridLayout_6.setSpacing(2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(2, 2, 2, 2)
        self.cb_multiStatic = QCheckBox(self.groupBox_5)
        self.cb_multiStatic.setObjectName(u"cb_multiStatic")

        self.gridLayout_6.addWidget(self.cb_multiStatic, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_5, 3, 0, 1, 3)

        self.apply_repnse = QPushButton(self.groupBox)
        self.apply_repnse.setObjectName(u"apply_repnse")

        self.gridLayout_2.addWidget(self.apply_repnse, 6, 2, 1, 1)

        self.gb_multi_static = QGroupBox(self.groupBox)
        self.gb_multi_static.setObjectName(u"gb_multi_static")
        self.gb_multi_static.setEnabled(False)
        self.gridLayout_5 = QGridLayout(self.gb_multi_static)
        self.gridLayout_5.setSpacing(2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(2, 2, 2, 2)
        self.btn_insert_static = QPushButton(self.gb_multi_static)
        self.btn_insert_static.setObjectName(u"btn_insert_static")
        self.btn_insert_static.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_5.addWidget(self.btn_insert_static, 0, 2, 1, 1)

        self.tb_mnode_static = QLineEdit(self.gb_multi_static)
        self.tb_mnode_static.setObjectName(u"tb_mnode_static")
        self.tb_mnode_static.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_5.addWidget(self.tb_mnode_static, 0, 1, 1, 1)

        self.tbl_static_mtp = QTableWidget(self.gb_multi_static)
        if (self.tbl_static_mtp.columnCount() < 1):
            self.tbl_static_mtp.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_static_mtp.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tbl_static_mtp.setObjectName(u"tbl_static_mtp")
        self.tbl_static_mtp.setStyleSheet(u"QHeaderView::section {background-color:green}")
        self.tbl_static_mtp.setFrameShape(QFrame.StyledPanel)
        self.tbl_static_mtp.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tbl_static_mtp.setAlternatingRowColors(True)
        self.tbl_static_mtp.setGridStyle(Qt.SolidLine)
        self.tbl_static_mtp.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_static_mtp.horizontalHeader().setStretchLastSection(True)
        self.tbl_static_mtp.verticalHeader().setProperty("showSortIndicator", False)
        self.tbl_static_mtp.verticalHeader().setStretchLastSection(False)

        self.gridLayout_5.addWidget(self.tbl_static_mtp, 1, 0, 1, 3)

        self.label_3 = QLabel(self.gb_multi_static)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.btn_delet_row_static = QPushButton(self.gb_multi_static)
        self.btn_delet_row_static.setObjectName(u"btn_delet_row_static")
        icon = QIcon()
        icon.addFile(u"icon/delete-row.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delet_row_static.setIcon(icon)

        self.gridLayout_5.addWidget(self.btn_delet_row_static, 2, 2, 1, 1)

        self.btn_add_roe_static = QPushButton(self.gb_multi_static)
        self.btn_add_roe_static.setObjectName(u"btn_add_roe_static")
        icon1 = QIcon()
        icon1.addFile(u"icon/add-row.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_roe_static.setIcon(icon1)

        self.gridLayout_5.addWidget(self.btn_add_roe_static, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.gb_multi_static, 5, 0, 1, 3)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_7 = QGridLayout(self.groupBox_3)
        self.gridLayout_7.setSpacing(2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(2, 2, 2, 2)
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1)

        self.cb_resp_component = QComboBox(self.groupBox_3)
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

        self.gridLayout_7.addWidget(self.cb_resp_component, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_3, 0, 0, 1, 3)


        self.gridLayout_8.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.PstaticWidget = PstaticWidget(self.groupBox_2)
        self.PstaticWidget.setObjectName(u"PstaticWidget")

        self.gridLayout_3.addWidget(self.PstaticWidget, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_14 = QGridLayout(self.tab_4)
        self.gridLayout_14.setSpacing(2)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(2, 2, 2, 2)
        self.groupBox_6 = QGroupBox(self.tab_4)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_11 = QGridLayout(self.groupBox_6)
        self.gridLayout_11.setSpacing(2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(2, 0, 2, 2)
        self.PushoverWidget = PushoverWidget(self.groupBox_6)
        self.PushoverWidget.setObjectName(u"PushoverWidget")

        self.gridLayout_11.addWidget(self.PushoverWidget, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_6, 0, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.tab_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(150, 0))
        self.groupBox_4.setMaximumSize(QSize(200, 16777215))
        self.gridLayout_9 = QGridLayout(self.groupBox_4)
        self.gridLayout_9.setSpacing(2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(2, 2, 2, 2)
        self.groupBox_7 = QGroupBox(self.groupBox_4)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_13 = QGridLayout(self.groupBox_7)
        self.gridLayout_13.setSpacing(2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(2, 2, 2, 2)
        self.label_6 = QLabel(self.groupBox_7)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_13.addWidget(self.label_6, 0, 0, 1, 1)

        self.cb_pushover_component = QComboBox(self.groupBox_7)
        self.cb_pushover_component.addItem("")
        self.cb_pushover_component.addItem("")
        self.cb_pushover_component.addItem("")
        self.cb_pushover_component.setObjectName(u"cb_pushover_component")

        self.gridLayout_13.addWidget(self.cb_pushover_component, 0, 1, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_7, 0, 0, 1, 2)

        self.gb_sigle_static_2 = QGroupBox(self.groupBox_4)
        self.gb_sigle_static_2.setObjectName(u"gb_sigle_static_2")
        self.gridLayout_10 = QGridLayout(self.gb_sigle_static_2)
        self.gridLayout_10.setSpacing(2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(2, 2, 2, 2)
        self.label_4 = QLabel(self.gb_sigle_static_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_10.addWidget(self.label_4, 1, 0, 1, 1)

        self.cb_pushover_nodenumber = QComboBox(self.gb_sigle_static_2)
        self.cb_pushover_nodenumber.setObjectName(u"cb_pushover_nodenumber")

        self.gridLayout_10.addWidget(self.cb_pushover_nodenumber, 1, 1, 1, 1)


        self.gridLayout_9.addWidget(self.gb_sigle_static_2, 2, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_2, 6, 1, 1, 1)

        self.gb_multi_static_2 = QGroupBox(self.groupBox_4)
        self.gb_multi_static_2.setObjectName(u"gb_multi_static_2")
        self.gb_multi_static_2.setEnabled(True)
        self.gridLayout_12 = QGridLayout(self.gb_multi_static_2)
        self.gridLayout_12.setSpacing(2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(2, 2, 2, 2)
        self.btn_insert_supportnode = QPushButton(self.gb_multi_static_2)
        self.btn_insert_supportnode.setObjectName(u"btn_insert_supportnode")
        self.btn_insert_supportnode.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_12.addWidget(self.btn_insert_supportnode, 0, 2, 1, 1)

        self.tb_supportnode = QLineEdit(self.gb_multi_static_2)
        self.tb_supportnode.setObjectName(u"tb_supportnode")
        self.tb_supportnode.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_12.addWidget(self.tb_supportnode, 0, 1, 1, 1)

        self.label_5 = QLabel(self.gb_multi_static_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)

        self.gridLayout_12.addWidget(self.label_5, 0, 0, 1, 1)

        self.btn_delete_roe_pushover = QPushButton(self.gb_multi_static_2)
        self.btn_delete_roe_pushover.setObjectName(u"btn_delete_roe_pushover")
        self.btn_delete_roe_pushover.setIcon(icon)

        self.gridLayout_12.addWidget(self.btn_delete_roe_pushover, 2, 2, 1, 1)

        self.btn_add_roe_pushover = QPushButton(self.gb_multi_static_2)
        self.btn_add_roe_pushover.setObjectName(u"btn_add_roe_pushover")
        self.btn_add_roe_pushover.setIcon(icon1)

        self.gridLayout_12.addWidget(self.btn_add_roe_pushover, 2, 1, 1, 1)

        self.tbl_pushover_supnode = QTableWidget(self.gb_multi_static_2)
        if (self.tbl_pushover_supnode.columnCount() < 1):
            self.tbl_pushover_supnode.setColumnCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_pushover_supnode.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        self.tbl_pushover_supnode.setObjectName(u"tbl_pushover_supnode")
        self.tbl_pushover_supnode.setStyleSheet(u"QHeaderView::section {background-color:green}\n"
"QHeaderView::section {color:white}\n"
"")
        self.tbl_pushover_supnode.setFrameShape(QFrame.StyledPanel)
        self.tbl_pushover_supnode.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tbl_pushover_supnode.setAlternatingRowColors(True)
        self.tbl_pushover_supnode.setGridStyle(Qt.SolidLine)
        self.tbl_pushover_supnode.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_pushover_supnode.horizontalHeader().setStretchLastSection(True)
        self.tbl_pushover_supnode.verticalHeader().setProperty("showSortIndicator", False)
        self.tbl_pushover_supnode.verticalHeader().setStretchLastSection(False)

        self.gridLayout_12.addWidget(self.tbl_pushover_supnode, 1, 0, 1, 3)


        self.gridLayout_9.addWidget(self.gb_multi_static_2, 4, 0, 1, 2)

        self.apply_pushover = QPushButton(self.groupBox_4)
        self.apply_pushover.setObjectName(u"apply_pushover")
        self.apply_pushover.setMaximumSize(QSize(85, 16777215))

        self.gridLayout_9.addWidget(self.apply_pushover, 5, 1, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 998, 21))
        self.savedata = QMenu(self.menubar)
        self.savedata.setObjectName(u"savedata")
        self.menuPlot_Setting_2 = QMenu(self.menubar)
        self.menuPlot_Setting_2.setObjectName(u"menuPlot_Setting_2")
        self.menuMajor_Grid_2 = QMenu(self.menuPlot_Setting_2)
        self.menuMajor_Grid_2.setObjectName(u"menuMajor_Grid_2")
        self.menuLine_Style = QMenu(self.menuMajor_Grid_2)
        self.menuLine_Style.setObjectName(u"menuLine_Style")
        self.menuLine_Width = QMenu(self.menuMajor_Grid_2)
        self.menuLine_Width.setObjectName(u"menuLine_Width")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.savedata.menuAction())
        self.menubar.addAction(self.menuPlot_Setting_2.menuAction())
        self.savedata.addAction(self.mb_savedata)
        self.savedata.addAction(self.actionSave_Pushover_Data)
        self.menuPlot_Setting_2.addAction(self.actionChange_Background_Color)
        self.menuPlot_Setting_2.addAction(self.menuMajor_Grid_2.menuAction())
        self.menuMajor_Grid_2.addAction(self.actionLine_Color_g)
        self.menuMajor_Grid_2.addAction(self.menuLine_Style.menuAction())
        self.menuMajor_Grid_2.addAction(self.menuLine_Width.menuAction())
        self.menuLine_Style.addAction(self.actionSolid)
        self.menuLine_Style.addAction(self.actionDotted)
        self.menuLine_Style.addAction(self.actionDashed)
        self.menuLine_Style.addAction(self.actionDashdot)
        self.menuLine_Width.addAction(self.action0_2)
        self.menuLine_Width.addAction(self.action0_4)
        self.menuLine_Width.addAction(self.action0_6)
        self.menuLine_Width.addAction(self.action0_8)
        self.menuLine_Width.addAction(self.action1)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Reponse Plot", None))
        self.actionSave_Plot.setText(QCoreApplication.translate("MainWindow", u"Save Plot", None))
        self.actionSave_Data.setText(QCoreApplication.translate("MainWindow", u"Save Data", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionChange_Background_Color.setText(QCoreApplication.translate("MainWindow", u"Change Background Color", None))
        self.actionLine_Style.setText(QCoreApplication.translate("MainWindow", u"Line Style", None))
        self.actionLine_Color.setText(QCoreApplication.translate("MainWindow", u"Line Color", None))
        self.actionLine_Width.setText(QCoreApplication.translate("MainWindow", u"Line Width", None))
        self.actionSolid.setText(QCoreApplication.translate("MainWindow", u"Solid", None))
        self.actionDotted.setText(QCoreApplication.translate("MainWindow", u"Dotted", None))
        self.actionDashed.setText(QCoreApplication.translate("MainWindow", u"Dashed", None))
        self.actionDashdot.setText(QCoreApplication.translate("MainWindow", u"Dashdot", None))
        self.action0_2.setText(QCoreApplication.translate("MainWindow", u"0.2", None))
        self.action0_4.setText(QCoreApplication.translate("MainWindow", u"0.4", None))
        self.action0_6.setText(QCoreApplication.translate("MainWindow", u"0.6", None))
        self.action0_8.setText(QCoreApplication.translate("MainWindow", u"0.8", None))
        self.action1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.actionLine_Color_g.setText(QCoreApplication.translate("MainWindow", u"Line Color", None))
        self.mb_savedata.setText(QCoreApplication.translate("MainWindow", u"Save Response Data", None))
        self.actionSave_Pushover_Data.setText(QCoreApplication.translate("MainWindow", u"Save Pushover Data", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Static Analysis Result", None))
        self.cb_dt_static.setText(QCoreApplication.translate("MainWindow", u"dt (s)          ", None))
        self.gb_sigle_static.setTitle(QCoreApplication.translate("MainWindow", u"Single Node", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Node Number", None))
        self.tb_dt_static.setText(QCoreApplication.translate("MainWindow", u"0.02", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Multiple Node Selection", None))
        self.cb_multiStatic.setText(QCoreApplication.translate("MainWindow", u"Multiple Node", None))
        self.apply_repnse.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.gb_multi_static.setTitle(QCoreApplication.translate("MainWindow", u"Multiple Node", None))
        self.btn_insert_static.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
        self.tb_mnode_static.setText(QCoreApplication.translate("MainWindow", u"5", None))
        ___qtablewidgetitem = self.tbl_static_mtp.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Node Tag", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Total Node Number", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Response", None))
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

        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Response Plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Response Plot", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Push Over Curve", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Static Analysis Result", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Displacement (x axis)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Component", None))
        self.cb_pushover_component.setItemText(0, QCoreApplication.translate("MainWindow", u"Ux", None))
        self.cb_pushover_component.setItemText(1, QCoreApplication.translate("MainWindow", u"Uy", None))
        self.cb_pushover_component.setItemText(2, QCoreApplication.translate("MainWindow", u"Uz", None))

        self.gb_sigle_static_2.setTitle(QCoreApplication.translate("MainWindow", u"Control Node", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Node Number", None))
        self.gb_multi_static_2.setTitle(QCoreApplication.translate("MainWindow", u"Base Support Node", None))
        self.btn_insert_supportnode.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
        self.tb_supportnode.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Total Node Number", None))
        ___qtablewidgetitem1 = self.tbl_pushover_supnode.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Node Tag", None));
        self.apply_pushover.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Pushover Curve", None))
        self.savedata.setTitle(QCoreApplication.translate("MainWindow", u"Save Data", None))
        self.menuPlot_Setting_2.setTitle(QCoreApplication.translate("MainWindow", u"Plot Setting", None))
        self.menuMajor_Grid_2.setTitle(QCoreApplication.translate("MainWindow", u"Major Grid", None))
        self.menuLine_Style.setTitle(QCoreApplication.translate("MainWindow", u"Line Style", None))
        self.menuLine_Width.setTitle(QCoreApplication.translate("MainWindow", u"Line Width", None))
    # retranslateUi

