# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DynamicResponseWindows.ui'
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
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QWidget)

from pdynamicwidget import PdynamicWidget
from respspectrawidget import RespspectraWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(998, 426)
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
        self.mb_savedata_timeseries = QAction(MainWindow)
        self.mb_savedata_timeseries.setObjectName(u"mb_savedata_timeseries")
        self.actionResponse_Spectra = QAction(MainWindow)
        self.actionResponse_Spectra.setObjectName(u"actionResponse_Spectra")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_8 = QGridLayout(self.tab_3)
        self.gridLayout_8.setSpacing(2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(2, 2, 2, 2)
        self.groupBox = QGroupBox(self.tab_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(150, 0))
        self.groupBox.setMaximumSize(QSize(200, 16777215))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.cb_dt_dynamic = QCheckBox(self.groupBox)
        self.cb_dt_dynamic.setObjectName(u"cb_dt_dynamic")

        self.gridLayout_2.addWidget(self.cb_dt_dynamic, 6, 0, 1, 1)

        self.gb_sigle_dynamic = QGroupBox(self.groupBox)
        self.gb_sigle_dynamic.setObjectName(u"gb_sigle_dynamic")
        self.gridLayout_4 = QGridLayout(self.gb_sigle_dynamic)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.label = QLabel(self.gb_sigle_dynamic)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)

        self.cb_resp_nodenumber = QComboBox(self.gb_sigle_dynamic)
        self.cb_resp_nodenumber.setObjectName(u"cb_resp_nodenumber")

        self.gridLayout_4.addWidget(self.cb_resp_nodenumber, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.gb_sigle_dynamic, 2, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 7, 2, 1, 1)

        self.tb_dt_dynamic = QLineEdit(self.groupBox)
        self.tb_dt_dynamic.setObjectName(u"tb_dt_dynamic")
        self.tb_dt_dynamic.setEnabled(False)

        self.gridLayout_2.addWidget(self.tb_dt_dynamic, 6, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_6 = QGridLayout(self.groupBox_5)
        self.gridLayout_6.setSpacing(2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(2, 2, 2, 2)
        self.cb_multiDynamic = QCheckBox(self.groupBox_5)
        self.cb_multiDynamic.setObjectName(u"cb_multiDynamic")

        self.gridLayout_6.addWidget(self.cb_multiDynamic, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_5, 3, 0, 1, 3)

        self.apply_repnse_dynamic = QPushButton(self.groupBox)
        self.apply_repnse_dynamic.setObjectName(u"apply_repnse_dynamic")

        self.gridLayout_2.addWidget(self.apply_repnse_dynamic, 6, 2, 1, 1)

        self.gb_multi_dynamic = QGroupBox(self.groupBox)
        self.gb_multi_dynamic.setObjectName(u"gb_multi_dynamic")
        self.gb_multi_dynamic.setEnabled(False)
        self.gridLayout_5 = QGridLayout(self.gb_multi_dynamic)
        self.gridLayout_5.setSpacing(2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(2, 2, 2, 2)
        self.btn_insert_dynamic = QPushButton(self.gb_multi_dynamic)
        self.btn_insert_dynamic.setObjectName(u"btn_insert_dynamic")
        self.btn_insert_dynamic.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_5.addWidget(self.btn_insert_dynamic, 0, 2, 1, 1)

        self.tb_mnode_dynamic = QLineEdit(self.gb_multi_dynamic)
        self.tb_mnode_dynamic.setObjectName(u"tb_mnode_dynamic")
        self.tb_mnode_dynamic.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_5.addWidget(self.tb_mnode_dynamic, 0, 1, 1, 1)

        self.tbl_dynamic_mtp = QTableWidget(self.gb_multi_dynamic)
        if (self.tbl_dynamic_mtp.columnCount() < 1):
            self.tbl_dynamic_mtp.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_dynamic_mtp.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tbl_dynamic_mtp.setObjectName(u"tbl_dynamic_mtp")
        self.tbl_dynamic_mtp.setStyleSheet(u"QHeaderView::section {background-color:green}\n"
"QHeaderView::section {color:white}\n"
"")
        self.tbl_dynamic_mtp.setFrameShape(QFrame.StyledPanel)
        self.tbl_dynamic_mtp.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tbl_dynamic_mtp.setAlternatingRowColors(True)
        self.tbl_dynamic_mtp.setGridStyle(Qt.SolidLine)
        self.tbl_dynamic_mtp.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_dynamic_mtp.horizontalHeader().setStretchLastSection(True)
        self.tbl_dynamic_mtp.verticalHeader().setProperty("showSortIndicator", False)
        self.tbl_dynamic_mtp.verticalHeader().setStretchLastSection(False)

        self.gridLayout_5.addWidget(self.tbl_dynamic_mtp, 1, 0, 1, 3)

        self.label_3 = QLabel(self.gb_multi_dynamic)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.btn_delet_row_dynamic = QPushButton(self.gb_multi_dynamic)
        self.btn_delet_row_dynamic.setObjectName(u"btn_delet_row_dynamic")
        icon = QIcon()
        icon.addFile(u"icon/delete-row.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delet_row_dynamic.setIcon(icon)

        self.gridLayout_5.addWidget(self.btn_delet_row_dynamic, 2, 2, 1, 1)

        self.btn_add_roe_dynamic = QPushButton(self.gb_multi_dynamic)
        self.btn_add_roe_dynamic.setObjectName(u"btn_add_roe_dynamic")
        icon1 = QIcon()
        icon1.addFile(u"icon/add-row.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_roe_dynamic.setIcon(icon1)

        self.gridLayout_5.addWidget(self.btn_add_roe_dynamic, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.gb_multi_dynamic, 5, 0, 1, 3)

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
        self.PdynamicWidget = PdynamicWidget(self.groupBox_2)
        self.PdynamicWidget.setObjectName(u"PdynamicWidget")

        self.gridLayout_3.addWidget(self.PdynamicWidget, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_14 = QGridLayout(self.tab_4)
        self.gridLayout_14.setSpacing(2)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(2, 2, 2, 2)
        self.groupBox_8 = QGroupBox(self.tab_4)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_15 = QGridLayout(self.groupBox_8)
        self.gridLayout_15.setSpacing(2)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(2, 2, 2, 2)
        self.RespspectraWidget = RespspectraWidget(self.groupBox_8)
        self.RespspectraWidget.setObjectName(u"RespspectraWidget")

        self.gridLayout_15.addWidget(self.RespspectraWidget, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_8, 0, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.tab_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(150, 0))
        self.groupBox_4.setMaximumSize(QSize(200, 16777215))
        self.gridLayout_9 = QGridLayout(self.groupBox_4)
        self.gridLayout_9.setSpacing(2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(2, 2, 2, 2)
        self.gb_sigle_static_4 = QGroupBox(self.groupBox_4)
        self.gb_sigle_static_4.setObjectName(u"gb_sigle_static_4")
        self.gridLayout_22 = QGridLayout(self.gb_sigle_static_4)
        self.gridLayout_22.setSpacing(2)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(2, 2, 2, 5)
        self.rbn_Sd = QRadioButton(self.gb_sigle_static_4)
        self.rbn_Sd.setObjectName(u"rbn_Sd")

        self.gridLayout_22.addWidget(self.rbn_Sd, 0, 2, 1, 1)

        self.rbn_PSa = QRadioButton(self.gb_sigle_static_4)
        self.rbn_PSa.setObjectName(u"rbn_PSa")
        self.rbn_PSa.setChecked(False)

        self.gridLayout_22.addWidget(self.rbn_PSa, 2, 0, 1, 1)

        self.rbn_Sa = QRadioButton(self.gb_sigle_static_4)
        self.rbn_Sa.setObjectName(u"rbn_Sa")
        self.rbn_Sa.setChecked(True)

        self.gridLayout_22.addWidget(self.rbn_Sa, 0, 0, 1, 1)

        self.rbn_PSv = QRadioButton(self.gb_sigle_static_4)
        self.rbn_PSv.setObjectName(u"rbn_PSv")

        self.gridLayout_22.addWidget(self.rbn_PSv, 2, 1, 1, 1)

        self.rbn_Sv = QRadioButton(self.gb_sigle_static_4)
        self.rbn_Sv.setObjectName(u"rbn_Sv")

        self.gridLayout_22.addWidget(self.rbn_Sv, 0, 1, 1, 1)


        self.gridLayout_9.addWidget(self.gb_sigle_static_4, 5, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.groupBox_4)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_19 = QGridLayout(self.groupBox_10)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setHorizontalSpacing(2)
        self.gridLayout_19.setVerticalSpacing(5)
        self.gridLayout_19.setContentsMargins(2, 2, 2, 2)
        self.label_15 = QLabel(self.groupBox_10)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_19.addWidget(self.label_15, 2, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_10)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_19.addWidget(self.label_11, 1, 0, 1, 1)

        self.tb_damping_rs = QLineEdit(self.groupBox_10)
        self.tb_damping_rs.setObjectName(u"tb_damping_rs")
        self.tb_damping_rs.setEnabled(True)

        self.gridLayout_19.addWidget(self.tb_damping_rs, 2, 1, 1, 1)

        self.tb_dt_rs = QLineEdit(self.groupBox_10)
        self.tb_dt_rs.setObjectName(u"tb_dt_rs")
        self.tb_dt_rs.setEnabled(True)

        self.gridLayout_19.addWidget(self.tb_dt_rs, 1, 1, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_10, 3, 0, 1, 1)

        self.gb_sigle_rs = QGroupBox(self.groupBox_4)
        self.gb_sigle_rs.setObjectName(u"gb_sigle_rs")
        self.gridLayout_10 = QGridLayout(self.gb_sigle_rs)
        self.gridLayout_10.setSpacing(2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(2, 2, 2, 2)
        self.label_4 = QLabel(self.gb_sigle_rs)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_10.addWidget(self.label_4, 1, 0, 1, 1)

        self.cb_resp_nodenumber_rs = QComboBox(self.gb_sigle_rs)
        self.cb_resp_nodenumber_rs.setObjectName(u"cb_resp_nodenumber_rs")

        self.gridLayout_10.addWidget(self.cb_resp_nodenumber_rs, 1, 1, 1, 1)


        self.gridLayout_9.addWidget(self.gb_sigle_rs, 1, 0, 1, 2)

        self.gb_sigle_static_3 = QGroupBox(self.groupBox_4)
        self.gb_sigle_static_3.setObjectName(u"gb_sigle_static_3")
        self.gridLayout_21 = QGridLayout(self.gb_sigle_static_3)
        self.gridLayout_21.setSpacing(2)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(2, 2, 2, 5)
        self.rbn_F = QRadioButton(self.gb_sigle_static_3)
        self.rbn_F.setObjectName(u"rbn_F")

        self.gridLayout_21.addWidget(self.rbn_F, 0, 1, 1, 1)

        self.rbn__T = QRadioButton(self.gb_sigle_static_3)
        self.rbn__T.setObjectName(u"rbn__T")
        self.rbn__T.setChecked(True)

        self.gridLayout_21.addWidget(self.rbn__T, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.gb_sigle_static_3, 4, 0, 1, 1)

        self.gb_sigle_static_5 = QGroupBox(self.groupBox_4)
        self.gb_sigle_static_5.setObjectName(u"gb_sigle_static_5")
        self.gridLayout_23 = QGridLayout(self.gb_sigle_static_5)
        self.gridLayout_23.setSpacing(2)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(2, 2, 2, 5)
        self.rbn_Ay = QRadioButton(self.gb_sigle_static_5)
        self.rbn_Ay.setObjectName(u"rbn_Ay")

        self.gridLayout_23.addWidget(self.rbn_Ay, 0, 1, 1, 1)

        self.rbn_Ax = QRadioButton(self.gb_sigle_static_5)
        self.rbn_Ax.setObjectName(u"rbn_Ax")
        self.rbn_Ax.setChecked(True)

        self.gridLayout_23.addWidget(self.rbn_Ax, 0, 0, 1, 1)

        self.rbn_Az = QRadioButton(self.gb_sigle_static_5)
        self.rbn_Az.setObjectName(u"rbn_Az")

        self.gridLayout_23.addWidget(self.rbn_Az, 0, 2, 1, 1)


        self.gridLayout_9.addWidget(self.gb_sigle_static_5, 2, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_3, 8, 0, 1, 1)

        self.apply_rs = QPushButton(self.groupBox_4)
        self.apply_rs.setObjectName(u"apply_rs")

        self.gridLayout_9.addWidget(self.apply_rs, 7, 0, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 1)

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
        self.savedata.addAction(self.mb_savedata_timeseries)
        self.savedata.addAction(self.actionResponse_Spectra)
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

        self.tabWidget.setCurrentIndex(1)


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
        self.mb_savedata_timeseries.setText(QCoreApplication.translate("MainWindow", u"Time Series Data", None))
        self.actionResponse_Spectra.setText(QCoreApplication.translate("MainWindow", u"Response Spectra", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Dynamic Analysis Result", None))
        self.cb_dt_dynamic.setText(QCoreApplication.translate("MainWindow", u"dt (s)          ", None))
        self.gb_sigle_dynamic.setTitle(QCoreApplication.translate("MainWindow", u"Single Node", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Node Number", None))
        self.tb_dt_dynamic.setText(QCoreApplication.translate("MainWindow", u"0.02", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Multiple Node Selection", None))
        self.cb_multiDynamic.setText(QCoreApplication.translate("MainWindow", u"Multiple Node", None))
        self.apply_repnse_dynamic.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.gb_multi_dynamic.setTitle(QCoreApplication.translate("MainWindow", u"Multiple Node", None))
        self.btn_insert_dynamic.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
        self.tb_mnode_dynamic.setText(QCoreApplication.translate("MainWindow", u"5", None))
        ___qtablewidgetitem = self.tbl_dynamic_mtp.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Node Tag", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Total Node Number", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Response", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Component", None))
        self.cb_resp_component.setItemText(0, QCoreApplication.translate("MainWindow", u"Ax", None))
        self.cb_resp_component.setItemText(1, QCoreApplication.translate("MainWindow", u"Ay", None))
        self.cb_resp_component.setItemText(2, QCoreApplication.translate("MainWindow", u"Az", None))
        self.cb_resp_component.setItemText(3, QCoreApplication.translate("MainWindow", u"Vx", None))
        self.cb_resp_component.setItemText(4, QCoreApplication.translate("MainWindow", u"Vy", None))
        self.cb_resp_component.setItemText(5, QCoreApplication.translate("MainWindow", u"Vz", None))
        self.cb_resp_component.setItemText(6, QCoreApplication.translate("MainWindow", u"Ux", None))
        self.cb_resp_component.setItemText(7, QCoreApplication.translate("MainWindow", u"Uy", None))
        self.cb_resp_component.setItemText(8, QCoreApplication.translate("MainWindow", u"Uz", None))
        self.cb_resp_component.setItemText(9, QCoreApplication.translate("MainWindow", u"Rx", None))
        self.cb_resp_component.setItemText(10, QCoreApplication.translate("MainWindow", u"Ry", None))
        self.cb_resp_component.setItemText(11, QCoreApplication.translate("MainWindow", u"Rz", None))
        self.cb_resp_component.setItemText(12, QCoreApplication.translate("MainWindow", u"RFx", None))
        self.cb_resp_component.setItemText(13, QCoreApplication.translate("MainWindow", u"RFy", None))
        self.cb_resp_component.setItemText(14, QCoreApplication.translate("MainWindow", u"RFz", None))
        self.cb_resp_component.setItemText(15, QCoreApplication.translate("MainWindow", u"RMx", None))
        self.cb_resp_component.setItemText(16, QCoreApplication.translate("MainWindow", u"RMy", None))
        self.cb_resp_component.setItemText(17, QCoreApplication.translate("MainWindow", u"RMz", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Response Plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Time Series", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Response Plot", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Dynamic Analysis Result", None))
        self.gb_sigle_static_4.setTitle(QCoreApplication.translate("MainWindow", u"Vertical Axis", None))
        self.rbn_Sd.setText(QCoreApplication.translate("MainWindow", u"Sd", None))
        self.rbn_PSa.setText(QCoreApplication.translate("MainWindow", u"PSa", None))
        self.rbn_Sa.setText(QCoreApplication.translate("MainWindow", u"Sa", None))
        self.rbn_PSv.setText(QCoreApplication.translate("MainWindow", u"PSv", None))
        self.rbn_Sv.setText(QCoreApplication.translate("MainWindow", u"Sv", None))
        self.groupBox_10.setTitle("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Damping Value", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Time Increment, dt     ", None))
        self.tb_damping_rs.setText(QCoreApplication.translate("MainWindow", u"0.05", None))
        self.tb_dt_rs.setText(QCoreApplication.translate("MainWindow", u"0.02", None))
        self.gb_sigle_rs.setTitle(QCoreApplication.translate("MainWindow", u"Single Node", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Node Number", None))
        self.gb_sigle_static_3.setTitle(QCoreApplication.translate("MainWindow", u"Horizontal Axis", None))
        self.rbn_F.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.rbn__T.setText(QCoreApplication.translate("MainWindow", u"Period", None))
        self.gb_sigle_static_5.setTitle(QCoreApplication.translate("MainWindow", u"Component", None))
        self.rbn_Ay.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.rbn_Ax.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.rbn_Az.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.apply_rs.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Response Spectra", None))
        self.savedata.setTitle(QCoreApplication.translate("MainWindow", u"Save Data", None))
        self.menuPlot_Setting_2.setTitle(QCoreApplication.translate("MainWindow", u"Plot Setting", None))
        self.menuMajor_Grid_2.setTitle(QCoreApplication.translate("MainWindow", u"Major Grid", None))
        self.menuLine_Style.setTitle(QCoreApplication.translate("MainWindow", u"Line Style", None))
        self.menuLine_Width.setTitle(QCoreApplication.translate("MainWindow", u"Line Width", None))
    # retranslateUi

