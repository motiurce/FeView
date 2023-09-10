# 이 파일이 메인파일로 현재 수정중임. - 이걸 분석해서 남들이 어떻게 인터페이스를 구성하는지 공부하자.
import cp as cp
from PySide6 import QtWidgets, QtCore, Qt
from PySide6.QtGui import (
    QAction,
    QGuiApplication,
)  # QDesktopWidget이 버전이 올라가면서 없어져서 QGuiApplication.primaryScreen()사용
from PySide6.QtWidgets import (
    QMessageBox,
    QFileDialog,
    QWidget,
    QColorDialog,
    QFontDialog,
    QDialog,
    QTableWidgetItem,
    QVBoxLayout,
    QSplashScreen,
    QProgressBar,
)
from PySide6.QtGui import QIcon, QPixmap
import sys, os, time
from webbrowser import open_new_tab
import xlwt
import subprocess as sp
from plotting import *
from mode import *
from recorder import *
from read_outfiles import *
from utilities import *
import matplotlib as mpl
from RS import *
import numpy as np
import pandas as pd
from pyvistaqt import QtInteractor

# PySide6에서 uic를 사용하는 방법이 PyQt5와 다르다. 따라서 ui를 바로 사용하지 않고 py로 만들어 사용
# pyside6-uic MainWindows.ui -o MainWindows.py과 같이 생성
# 내부 클래스 명이 전부 Ui_MainWindow이므로, 이를 변경하여 사용
from UI.DataTable_Dynamic import Ui_MainWindow as UI_DataTable_Dynamic
from UI.DataTable_Static import Ui_MainWindow as UI_DataTable_Static
from UI.DataTable_Modal import Ui_MainWindow as UI_DataTable_Modal
from UI.DynamicResponseWindows import Ui_MainWindow as UI_DynamicResponseWindows
from UI.StaticResponseWindows import Ui_MainWindow as UI_StaticResponseWindows
from UI.LoadSetting import Ui_MainWindow as UI_LoadSetting
from UI.MainWindows import Ui_MainWindow as UI_MainWindows
from UI.ResponseWindows import Ui_MainWindow as UI_ResponseWindows
from UI.about import Ui_MainWindow as UI_about

main = None


class FeViewMain(QtWidgets.QMainWindow, UI_MainWindows):
    def __init__(self, parent=None):
        super(FeViewMain, self).__init__(parent)
        # windows에서 경로 표시할 경우 /로 표기, 맥에서 경로 표기시 \로 표기
        # uic.loadUi('UI/MainWindows.ui', self)
        # load MainWindows.ui from Qt Designer- 상속받아 사용하므로 아래와 같이 변경함
        self.setupUi(self)
        # add the pyvista interactor object
        vlayout = QVBoxLayout()
        self.p = self.plot_widget = QtInteractor(self.frame)
        self.p.show_axes()
        vlayout.addWidget(self.plot_widget.interactor)
        self.frame.setLayout(vlayout)
        self.setCentralWidget(self.frame)
        vlayout.setContentsMargins(0, 0, 0, 0)
        # add some toolbar
        self.btn_tool_openTCL = QAction(
            QIcon("UI/icon/Open.png"), "Open TCL File", self
        )
        self.btn_tool_editTCL = QAction(
            QIcon("UI/icon/edit.png"), "Edit TCL File", self
        )
        self.btn_tool_run_OS = QAction(
            QIcon("UI/icon/run.png"), "run TCL file with OpenSees", self
        )
        self.btn_iso = QAction(QIcon("UI/icon/iso.png"), "View isometric", self)
        self.btn_iso.setCheckable(True)  # toolbar button checkable
        self.btn_xy_zpluss = QAction(
            QIcon("UI/icon/xy_zpluss.png"), "View xy_zpluss", self
        )
        self.btn_xy_zpluss.setCheckable(True)
        self.btn_xy_zminus = QAction(
            QIcon("UI/icon/xy_zminus.png"), "View xy_zminus", self
        )
        self.btn_xy_zminus.setCheckable(True)
        self.btn_xz_ypluss = QAction(
            QIcon("UI/icon/xz_ypluss.png"), "View xz_ypluss", self
        )
        self.btn_xz_ypluss.setCheckable(True)
        self.btn_xz_yminus = QAction(
            QIcon("UI/icon/xz_yminus.png"), "View xz_yminus", self
        )
        self.btn_xz_yminus.setCheckable(True)
        self.btn_yz_xpluss = QAction(
            QIcon("UI/icon/yz_xpluss.png"), "View yz_xpluss", self
        )
        self.btn_yz_xpluss.setCheckable(True)
        self.btn_yz_xminus = QAction(
            QIcon("UI/icon/yz_xminus.png"), "View yz_xminus", self
        )
        self.btn_yz_xminus.setCheckable(True)
        self.btn_node_label = QAction(QIcon("UI/icon/nl.png"), "View Node Label", self)
        self.btn_node_label.setCheckable(True)
        self.btn_node_cord = QAction(
            QIcon("UI/icon/nc.png"), "View Node Co-ordinate", self
        )
        self.btn_node_cord.setCheckable(True)
        self.btn_load = QAction(QIcon("UI/icon/load.png"), "View Point Load", self)
        self.btn_load.setCheckable(True)
        self.btn_color_plot_background = QAction(
            QIcon("UI/icon/color_plot_background.png"),
            "Change Plot Background Color",
            self,
        )
        self.btn_color_gui = QAction(
            QIcon("UI/icon/color_gui.png"), "Change Theme Color", self
        )
        self.btn_font = QAction(QIcon("UI/icon/font.png"), "Change Font Style", self)
        self.btn_plot_image = QAction(
            QIcon("UI/icon/plot_image.png"), "Save Plot as Image", self
        )
        self.btn_plot_image_wb = QAction(
            QIcon("UI/icon/plot_image_wb.png"),
            "Save Plot as Image with White Background",
            self,
        )
        self.btn_calc = QAction(QIcon("UI/icon/calculator.png"), "Calculator", self)
        self.btn_minumize = QAction(
            QIcon("UI/icon/minimize.png"), "Mimimize the Window", self
        )
        self.btn_maximize = QAction(
            QIcon("UI/icon/maximize.png"), "Maximize the Window", self
        )
        self.btn_full_s = QAction(QIcon("UI/icon/full_s.png"), "Fullscreen", self)
        self.btn_center = QAction(QIcon("UI/icon/center.png"), "Center", self)
        self.btn_min_s = QAction(QIcon("UI/icon/min.png"), "Minimum Window Size", self)
        self.btn_max_s = QAction(QIcon("UI/icon/max.png"), "Maximum Window Size", self)
        self.btn_restore = QAction(QIcon("UI/icon/rest_w.png"), "Restore Window", self)
        self.btn_help = QAction(QIcon("UI/icon/help.png"), "Help", self)
        self.btn_about = QAction(QIcon("UI/icon/info.png"), "Info", self)
        self.btn_close = QAction(QIcon("UI/icon/close.png"), "Exir", self)
        toolbar = self.addToolBar("Exit")
        toolbar.addAction(self.btn_tool_openTCL)
        toolbar.addAction(self.btn_tool_editTCL)
        toolbar.addAction(self.btn_tool_run_OS)
        toolbar.addSeparator()
        toolbar.addAction(self.btn_iso)
        toolbar.addAction(self.btn_xy_zpluss)
        toolbar.addAction(self.btn_xy_zminus)
        toolbar.addAction(self.btn_xz_ypluss)
        toolbar.addAction(self.btn_xz_yminus)
        toolbar.addAction(self.btn_yz_xpluss)
        toolbar.addAction(self.btn_yz_xminus)
        toolbar.addSeparator()  # add separator
        toolbar.addAction(self.btn_node_label)
        toolbar.addAction(self.btn_node_cord)
        toolbar.addAction(self.btn_load)
        toolbar.addSeparator()
        toolbar.addAction(self.btn_color_plot_background)
        toolbar.addAction(self.btn_color_gui)
        toolbar.addAction(self.btn_font)
        toolbar.addSeparator()
        toolbar.addAction(self.btn_plot_image)
        toolbar.addAction(self.btn_plot_image_wb)
        toolbar.addAction(self.btn_calc)
        toolbar.addSeparator()
        toolbar.addAction(self.btn_minumize)
        toolbar.addAction(self.btn_maximize)
        toolbar.addAction(self.btn_full_s)
        toolbar.addAction(self.btn_center)
        toolbar.addAction(self.btn_min_s)
        toolbar.addAction(self.btn_max_s)
        toolbar.addAction(self.btn_restore)
        toolbar.addSeparator()
        toolbar.addAction(self.btn_help)
        toolbar.addAction(self.btn_about)
        toolbar.addAction(self.btn_close)
        toolbar.addSeparator()
        # margin & layout setting for toolbar
        toolbar.setContentsMargins(0, 0, 0, 0)
        toolbar.layout().setSpacing(0)
        toolbar.layout().setContentsMargins(0, 0, 0, 0)
        self.btn_tool_openTCL.triggered.connect(
            self.openTCL
        )  # call function for 'Open TCL file' toolbar button
        self.actionOpen.triggered.connect(
            self.openTCL
        )  # call function for 'Open TCL file' main manu button
        self.btn_apply_static.clicked.connect(self.DispStatic)
        self.actionApply_Static.triggered.connect(self.DispStatic)

        self.btn_apply_modal.clicked.connect(self.DispModal)
        self.actionApply_Modal.triggered.connect(self.DispModal)
        self.btn_apply_dynamic.clicked.connect(self.DispDynamic)
        self.Apply_Dyanamic.triggered.connect(self.DispDynamic)
        self.btn_response_static.clicked.connect(self.res_static)
        self.actionShow_Response.triggered.connect(self.res_static)
        self.btn_response_dynamic.clicked.connect(self.res_dynamic)
        self.actionShow_Response_dynamic.triggered.connect(self.res_dynamic)
        self.btn_tool_editTCL.triggered.connect(self.edit_TCL)
        self.actionEdit.triggered.connect(self.edit_TCL)
        self.btn_tool_run_OS.triggered.connect(self.runOS)
        self.actionRun_OpenSees.triggered.connect(self.runOS)
        self.btn_iso.triggered.connect(self.iso)
        self.btn_xy_zpluss.triggered.connect(self.xy_zpluss)
        self.btn_xy_zminus.triggered.connect(self.xy_zminus)
        self.btn_xz_ypluss.triggered.connect(self.xz_ypluss)
        self.btn_xz_yminus.triggered.connect(self.xz_yminus)
        self.btn_yz_xpluss.triggered.connect(self.yz_xpluss)
        self.btn_yz_xminus.triggered.connect(self.yz_xminus)
        self.actionFeView.triggered.connect(self.about_feview)
        self.btn_about.triggered.connect(self.about_feview)
        self.actionPlot_Background_Color.triggered.connect(self.Plot_Background_Color)
        self.btn_color_plot_background.triggered.connect(self.Plot_Background_Color)
        self.actionGUI_Font.triggered.connect(self.GUI_Font)
        self.btn_font.triggered.connect(self.GUI_Font)
        self.actionTheme_Color.triggered.connect(self.gui_color)
        self.btn_color_gui.triggered.connect(self.gui_color)
        self.btn_plot_image.triggered.connect(self.savePlot)
        self.actionWith_background.triggered.connect(self.savePlot)
        self.btn_plot_image_wb.triggered.connect(self.savePlot_wb)
        self.actionWhite_Background.triggered.connect(self.savePlot_wb)
        self.btn_calc.triggered.connect(self.calculator)
        self.actionMinimize.triggered.connect(lambda: self.showMinimized())
        self.btn_minumize.triggered.connect(lambda: self.showMinimized())
        self.actionMaximize.triggered.connect(lambda: self.showMaximized())
        self.btn_maximize.triggered.connect(lambda: self.showMaximized())
        self.actionFull_Screen.triggered.connect(lambda: self.showFullScreen())
        self.btn_full_s.triggered.connect(lambda: self.showFullScreen())
        self.actionCenter.triggered.connect(lambda: self.center())
        self.btn_center.triggered.connect(lambda: self.center())
        self.actionMinimum_Size.triggered.connect(
            lambda: self.resize(self.minimumSize())
        )
        self.btn_min_s.triggered.connect(lambda: self.resize(self.minimumSize()))
        self.actionMaximum_Size.triggered.connect(
            lambda: self.resize(self.maximumSize())
        )
        self.btn_max_s.triggered.connect(lambda: self.resize(self.maximumSize()))

        self.actionRestore.triggered.connect(lambda: self.showNormal())
        self.btn_restore.triggered.connect(lambda: self.showNormal())
        self.actionSSL.triggered.connect(lambda: open_new_tab("Help\FeView_Help.chm"))
        self.btn_help.triggered.connect(lambda: open_new_tab("Help\FeView_Help.chm"))

        self.actionOpenSees.triggered.connect(
            lambda: open_new_tab("https://opensees.berkeley.edu")
        )
        self.actionSSL_Website.triggered.connect(
            lambda: open_new_tab("http://www.kim2kie.com/3_ach/SSL_Software.php")
        )
        self.actionFeView_Website.triggered.connect(
            lambda: open_new_tab("http://www.kim2kie.com/3_ach/FeView/FeView.php")
        )

        self.btn_node_label.triggered.connect(self.nodelebels)
        self.actionNode_Label.triggered.connect(self.nodelebels)

        self.btn_node_cord.triggered.connect(self.nodecoordinates)
        self.actionNode_Coordinate.triggered.connect(self.nodecoordinates)
        self.btn_load.triggered.connect(self.pointload_show)
        self.actionLoad.triggered.connect(self.pointload_show)

        self.actionExit.triggered.connect(self.close)
        self.btn_close.triggered.connect(self.close)
        self.actionMesh_Fiew.triggered.connect(self.mesh_view_model)
        self.actionSmooth_View.triggered.connect(self.smoth_view_model)
        self.actionWireframe.triggered.connect(self.wiremesh_model)
        self.actionMesh_View_2.triggered.connect(self.mesh_view_model_deform)
        self.actionSmooth_View_2.triggered.connect(self.smoth_view_model_deform)
        self.actionMesh_View_Wiremesh_undeform.triggered.connect(
            self.mesh_wiremesh_model_deform
        )
        self.actionSmooth_View_Wiremesh_undeform.triggered.connect(
            self.smooth_wiremesh_model_deform
        )
        self.btn_datatable_static.clicked.connect(self.data_table_static)
        self.actionData_Table.triggered.connect(self.data_table_static)
        self.btn_datatable_modal.clicked.connect(self.data_table_modal)
        self.actionData_Table_modal.triggered.connect(self.data_table_modal)
        self.btn_datatable_dynamic.clicked.connect(self.data_table_dynamic)
        self.actionData_Table_dynamic.triggered.connect(self.data_table_dynamic)
        self.actionView_load.triggered.connect(self.load_setting_arrow)

        self.reportEdit.keyReleaseEvent = self.handleKeyRelease
        self.addInfoText("Opend tcl file")

        self.prgb = QProgressBar(self)
        self.statusBar().addPermanentWidget(self.prgb)

        self.dialogs = list()

    def progress(self, value, newLines):
        # self.te.append('\n'.join(newLines))
        self.prgb.setValue(value)

    def addInfoText(self, text):
        """Adds info text"""
        return self.reportEdit.insertPlainText("\n >>" + str(text))

    def handleKeyRelease(self, event):
        """Handles key inputs to report box"""
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.interpretUserInput(self.reportEdit.toPlainText())

    # function to unchecked another model display style setting except 'mesh view'

    def mesh_view_model(self):
        self.actionSmooth_View.setChecked(False)
        self.actionWireframe.setChecked(False)

    # function to unchecked another model display style setting except 'smooth view'

    def smoth_view_model(self):
        self.actionMesh_Fiew.setChecked(False)
        self.actionWireframe.setChecked(False)

    # function to unchecked another model display style setting except 'wiremesh view'

    def wiremesh_model(self):
        self.actionMesh_Fiew.setChecked(False)
        self.actionSmooth_View.setChecked(False)

    # function to unchecked another deform model display style setting except 'mesh view'

    def mesh_view_model_deform(self):
        self.actionSmooth_View_2.setChecked(False)
        self.actionMesh_View_Wiremesh_undeform.setChecked(False)
        self.actionSmooth_View_Wiremesh_undeform.setChecked(False)

    # function to unchecked another deform model display style setting except 'smooth view'

    def smoth_view_model_deform(self):
        self.actionMesh_View_2.setChecked(False)
        self.actionMesh_View_Wiremesh_undeform.setChecked(False)
        self.actionSmooth_View_Wiremesh_undeform.setChecked(False)

    # function to unchecked another deform model display style setting except 'mesh view+wiremesh'
    def mesh_wiremesh_model_deform(self):
        self.actionMesh_View_2.setChecked(False)
        self.actionSmooth_View_2.setChecked(False)
        self.actionSmooth_View_Wiremesh_undeform.setChecked(False)

    # function to unchecked another deform model display style setting except 'smooth view+wiremesh'
    def smooth_wiremesh_model_deform(self):
        self.actionMesh_View_2.setChecked(False)
        self.actionSmooth_View_2.setChecked(False)
        self.actionMesh_View_Wiremesh_undeform.setChecked(False)

    def openTCL(self):
        try:
            global numModes  # set numModes as global variable
            # create file dialog function to browse file path
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            self.fileName, _ = QFileDialog.getOpenFileName(
                self, "OpenSees File", "", "OpenSees File (*.tcl)", options=options
            )
            self.file_path, self.file_name = os.path.split(self.fileName)
            [filename0, sep, ext] = self.file_name.partition(".")
            # make path for output files
            self.result_directory = os.path.join(
                self.file_path, r"out_files_%s" % filename0
            )
            if not os.path.exists(self.result_directory):
                # create directory for output files
                os.mkdir(self.result_directory)
            # clear all actors from plot interface
            self.prgb.setMaximum(len(node(self.fileName)))
            self.p.clear()
            if self.actionSmooth_View.isChecked() == True:
                # call plotter considering smooth view
                plotter(
                    self.p,
                    self.fileName,
                    "smooth_view",
                    NodeCoords(self.fileName),
                    None,
                    None,
                )
            elif self.actionWireframe.isChecked() == True:
                # call plotter considering wiremesh view
                plotter(
                    self.p,
                    self.fileName,
                    "wireframe",
                    NodeCoords(self.fileName),
                    None,
                    None,
                )
            elif self.actionMesh_Fiew.isChecked() == True:
                # call plotter considering mesh view
                plotter(
                    self.p,
                    self.fileName,
                    "mesh_view",
                    NodeCoords(self.fileName),
                    None,
                    None,
                )
            # plotter_rigiddiaphram(self.p, self.fileName, NodeCoords(self.fileName))
            if (ndm_v(self.fileName)) == 2:
                self.p.view_xy()  # initial setting for 2d interface considering x-y axis view
            else:
                self.p.view_isometric()  # initial setting for 3d interface considering isometric view
            # read number of modes as "numModes"
            numModes = modeNumber(self.fileName)
            # clear previous item from "Mode Num." Combobox
            self.cb_numNodes.clear()

            if numModes.size > 0:
                for i in range(int(numModes)):
                    # add item to "Mode Num." combobox as Mode_1...
                    self.cb_numNodes.addItem("Mode_" + str(i + 1))
            (
                self.recorder_disp,
                self.recorder_rot,
                self.recorder_force,
                self.recorder_moment,
                self.recorder_accel,
                self.recorder_vel,
            ) = recorder_types(self.fileName)
            if self.recorder_disp == 1:
                # add item to "Component" combobox for displacement in static analysis result
                self.cb_node_contour_static.addItem(
                    "Displacement, Ux",
                )
                self.cb_node_contour_static.addItem("Displacement, Uy")
                self.cb_node_contour_static.addItem("Displacement, Uz")
                self.cb_node_contour_static.addItem("Displacement, Uxyz")
            if self.recorder_rot == 1:
                # add item to "Component" combobox for rotation in static analysis result
                self.cb_node_contour_static.addItem("Rotation, Rx")
                self.cb_node_contour_static.addItem("Rotation, Ry")
                self.cb_node_contour_static.addItem("Rotation, Rz")
                self.cb_node_contour_static.addItem("Rotation, Rxyz")
            if self.recorder_force == 1:
                # add item to "Component" combobox for force reaction in static analysis result
                self.cb_node_contour_static.addItem("Force Reaction, RFx")
                self.cb_node_contour_static.addItem("Force Reaction, RFy")
                self.cb_node_contour_static.addItem("Force Reaction, RFz")
                self.cb_node_contour_static.addItem("Force Reaction, RFxyz")
            if self.recorder_moment == 1:
                # add item to "Component" combobox for moment reaction in static analysis result
                self.cb_node_contour_static.addItem("Moment Reaction, RMx")
                self.cb_node_contour_static.addItem("Moment Reaction, RMy")
                self.cb_node_contour_static.addItem("Moment Reaction, RMz")
                self.cb_node_contour_static.addItem("Moment Reaction, RMxyz")
            if self.recorder_disp == 1:
                # add item to "Component" combobox for displacement in dynamic analysis result
                self.cb_node_contour_dynamic.addItem("Displacement, Ux")
                self.cb_node_contour_dynamic.addItem("Displacement, Uy")
                self.cb_node_contour_dynamic.addItem("Displacement, Uz")
                self.cb_node_contour_dynamic.addItem("Displacement, Uxyz")
            if self.recorder_rot == 1:
                # add item to "Component" combobox for rotation in dynamic analysis result
                self.cb_node_contour_dynamic.addItem("Rotation, Rx")
                self.cb_node_contour_dynamic.addItem("Rotation, Ry")
                self.cb_node_contour_dynamic.addItem("Rotation, Rz")
                self.cb_node_contour_dynamic.addItem("Rotation, Rxyz")
            if self.recorder_force == 1:
                # add item to "Component" combobox for force reaction in dynamic analysis result
                self.cb_node_contour_dynamic.addItem("Force Reaction, RFx")
                self.cb_node_contour_dynamic.addItem("Force Reaction, RFy")
                self.cb_node_contour_dynamic.addItem("Force Reaction, RFz")
                self.cb_node_contour_dynamic.addItem("Force Reaction, RFxyz")
            if self.recorder_moment == 1:
                # add item to "Component" combobox for moment reaction in dynamic analysis result
                self.cb_node_contour_dynamic.addItem("Moment Reaction, RMx")
                self.cb_node_contour_dynamic.addItem("Moment Reaction, RMy")
                self.cb_node_contour_dynamic.addItem("Moment Reaction, RMz")
                self.cb_node_contour_dynamic.addItem("Moment Reaction, RMxyz")
            if self.recorder_accel == 1:
                # add item to "Component" combobox for acceleration in dynamic analysis result
                self.cb_node_contour_dynamic.addItem("Acceleration, Ax")
                self.cb_node_contour_dynamic.addItem("Acceleration, Ay")
                self.cb_node_contour_dynamic.addItem("Acceleration, Az")
                self.cb_node_contour_dynamic.addItem("Acceleration, Axyz")
            if self.recorder_vel == 1:
                # add item to "Component" combobox for velocity in dynamic analysis result
                self.cb_node_contour_dynamic.addItem("Velocity, Vx")
                self.cb_node_contour_dynamic.addItem("Velocity, Vy")
                self.cb_node_contour_dynamic.addItem("Velocity, Vz")
                self.cb_node_contour_dynamic.addItem("Velocity, Vxyz")
            self.setWindowTitle(
                # windows title to show file path and filename
                "{}[*] - {}".format((self.fileName + " [" + filename0) + "]", "FeView")
            )
            try:
                # show total node and element in status bar
                self.statusBar().showMessage(
                    "Total Node : "
                    + str(len(node(self.fileName)))
                    + "; Total Element :"
                    + total_element(self.fileName)
                )
            except:
                QMessageBox.critical(self, "Error", "No node or element found")

            if self.actionView_load.isChecked() == True:
                # show point load
                point_load(
                    self.fileName,
                    self.p,
                    load_arrow_size,
                    load_font_size,
                    load_arrow_color,
                    load_font_color,
                )
            if self.actionView_Support.isChecked() == True:
                # show support
                support(self.fileName, self.p)

            self.addInfoText("Successfully loaded file \n" + self.fileName)

        except:
            QMessageBox.critical(self, "Error", "Please check TCL file")

    def DispStatic(self):
        try:
            self.btn_apply_modal.setChecked(False)
            self.btn_apply_dynamic.setChecked(False)
            scalefactor = float(
                self.tb_sef_scale_factor.text()
            )  # scale factor for diformation (static, modal and dynamic analysis)
            if self.recorder_disp == 1:
                # read output files for displacement
                self.outdispFile = OpenSeesOutputRead(
                    os.path.join(self.result_directory, "Node_displacements.out")
                )
                if step_static(self.fileName).size > 0:
                    # number of steps for static (if dynamic/transient analysis also included)
                    self.step_statics = int(step_static(self.fileName))
                else:
                    # number of steps for only static analysis
                    self.step_statics = len(self.outdispFile[:, 1])
                self.step_dynamic = (
                    len(self.outdispFile[:, 1]) - self.step_statics
                )  # steps for transient analysis
            if self.recorder_disp == 1:
                # read output files for displacement
                self.deformation = out_response(
                    (os.path.join(self.result_directory, "Node_displacements.out")),
                    self.step_statics,
                    ndm_v(self.fileName),
                    "all",
                )
                self.dispNodeCoords = NodeCoords(self.fileName) + (
                    scalefactor * self.deformation
                )
            if self.recorder_rot == 1:
                # read output files for rotation
                self.rotation = out_response(
                    (os.path.join(self.result_directory, "Node_rotations.out")),
                    self.step_statics,
                    ndm_v(self.fileName),
                    "rotation_moment",
                )
                self.outrotFile = OpenSeesOutputRead(
                    os.path.join(self.result_directory, "Node_rotations.out")
                )
            if self.recorder_force == 1:
                # read output files for force reaction
                self.forcereaction = out_response(
                    (os.path.join(self.result_directory, "Node_forceReactions.out")),
                    self.step_statics,
                    ndm_v(self.fileName),
                    "all",
                )
                self.outfreactFile = OpenSeesOutputRead(
                    os.path.join(self.result_directory, "Node_forceReactions.out")
                )
            if self.recorder_moment == 1:
                # read output files for moment reaction
                self.momentreaction = out_response(
                    (os.path.join(self.result_directory, "Node_momentReactions.out")),
                    self.step_statics,
                    ndm_v(self.fileName),
                    "rotation_moment",
                )
                self.outmreactFile = OpenSeesOutputRead(
                    os.path.join(self.result_directory, "Node_momentReactions.out")
                )
            self.p.clear()
            node_contour_type = (
                self.cb_node_contour_static.currentText()
            )  # get current text from "Component" combobox (Static result)
            if self.actionMesh_View_2.isChecked() == True:
                if node_contour_type == "Displacement, Ux":
                    scalars = self.deformation[:, 0]
                    d_max_x = np.max(np.abs(self.deformation[:, 0]))
                    stitle = "Displacement, Ux (Max. = " + str(d_max_x) + ")\n"
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Displacement, Uy":
                    scalars = self.deformation[:, 1]
                    d_max_y = np.max(np.abs(self.deformation[:, 1]))
                    stitle = "Displacement, Uy (Max. = " + str(d_max_y) + ")\n"
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Displacement, Uz":
                    scalars = self.deformation[:, 2]
                    d_max_z = np.max(np.abs(self.deformation[:, 2]))
                    stitle = "Displacement, Uz (Max. = " + str(d_max_z) + ")\n"
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Displacement, Uxyz":
                    scalars = self.deformation[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    d_max_xyz = np.max(np.abs(scalars))
                    stitle = "Displacement, Uxyz (Max. = " + str(d_max_xyz) + ")\n"
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Rotation, Rx":
                    scalars = self.rotation[:, 0]
                    stitle = (
                        "Rotation, Rx (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Rotation, Ry":
                    scalars = self.rotation[:, 1]
                    stitle = (
                        "Rotation, Ry (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Rotation, Rz":
                    scalars = self.rotation[:, 2]
                    stitle = (
                        "Rotation, Rz (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Rotation, Rxyz":
                    scalars = self.rotation[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Rotation, Rxyz (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Force Reaction, RFx":
                    scalars = self.forcereaction[:, 0]
                    stitle = (
                        "Force Reaction, RFx (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Force Reaction, RFy":
                    scalars = self.forcereaction[:, 1]
                    stitle = (
                        "Force Reaction, RFy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Force Reaction, RFz":
                    scalars = self.forcereaction[:, 2]
                    stitle = (
                        "Force Reaction, RFz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Force Reaction, RFxyz":
                    scalars = self.forcereaction[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Force Reaction, RFxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Moment Reaction, RMx":
                    scalars = self.momentreaction[:, 0]
                    stitle = (
                        "Moment Reaction, RMx (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Moment Reaction, RMy":
                    scalars = self.momentreaction[:, 1]
                    stitle = (
                        "Moment Reaction, RMy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    # stitle = 'Moment Reaction, RMx\n'
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Moment Reaction, RMz":
                    scalars = self.momentreaction[:, 2]
                    stitle = (
                        "Moment Reaction, RMz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    # stitle = 'Moment Reaction, RMz\n'
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Moment Reaction, RMxyz":
                    scalars = self.momentreaction[:, :3]
                    stitle = (
                        "Moment Reaction, RMxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )

            elif self.actionSmooth_View_2.isChecked() == True:
                if node_contour_type == "Displacement, Ux":
                    scalars = self.deformation[:, 0]
                    d_max_x = np.max(np.abs(self.deformation[:, 0]))
                    stitle = "Displacement, Ux (Max. = " + str(d_max_x) + ")\n"
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Displacement, Uy":
                    scalars = self.deformation[:, 1]
                    d_max_y = np.max(np.abs(self.deformation[:, 1]))
                    stitle = "Displacement, Uy (Max. = " + str(d_max_y) + ")\n"
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Displacement, Uz":
                    scalars = self.deformation[:, 2]
                    d_max_z = np.max(np.abs(self.deformation[:, 2]))
                    stitle = "Displacement, Uz (Max. = " + str(d_max_z) + ")\n"
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Displacement, Uxyz":
                    scalars = self.deformation[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    d_max_xyz = np.max(np.abs(scalars))
                    stitle = "Displacement, Uxyz (Max. = " + str(d_max_xyz) + ")\n"
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Rotation, Rx":
                    scalars = self.rotation[:, 2]
                    stitle = (
                        "Rotation, Rx (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Rotation, Ry":
                    scalars = self.rotation[:, 1]
                    stitle = (
                        "Rotation, Ry (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Rotation, Rz":
                    scalars = self.rotation[:, 0]
                    stitle = (
                        "Rotation, Rz (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Rotation, Rxyz":
                    scalars = self.rotation[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Rotation, Rxyz (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Force Reaction, RFx":
                    scalars = self.forcereaction[:, 0]
                    stitle = (
                        "Force Reaction, RFx (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Force Reaction, RFy":
                    scalars = self.forcereaction[:, 1]
                    stitle = (
                        "Force Reaction, RFy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    # stitle = 'Force Reaction, RFy\n'
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Force Reaction, RFz":
                    scalars = self.forcereaction[:, 2]
                    stitle = (
                        "Force Reaction, RFz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Force Reaction, RFxyz":
                    scalars = self.forcereaction[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Force Reaction, RFxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Moment Reaction, RMx":
                    scalars = self.momentreaction[:, 2]
                    stitle = (
                        "Moment Reaction, RMx (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Moment Reaction, RMy":
                    scalars = self.momentreaction[:, 1]
                    stitle = (
                        "Moment Reaction, RMy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    # stitle = 'Moment Reaction, RMx\n'
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Moment Reaction, RMz":
                    scalars = self.momentreaction[:, 0]
                    stitle = (
                        "Moment Reaction, RMz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    # stitle = 'Moment Reaction, RMz\n'
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Moment Reaction, RMxyz":
                    scalars = self.momentreaction[:, :3]
                    stitle = (
                        "Moment Reaction, RMxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )

            elif self.actionMesh_View_Wiremesh_undeform.isChecked() == True:
                if node_contour_type == "Displacement, Ux":
                    scalars = self.deformation[:, 0]
                    d_max_x = np.max(np.abs(self.deformation[:, 0]))
                    stitle = "Displacement, Ux (Max. = " + str(d_max_x) + ")\n"
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Displacement, Uy":
                    scalars = self.deformation[:, 1]
                    d_max_y = np.max(np.abs(self.deformation[:, 1]))
                    stitle = "Displacement, Uy (Max. = " + str(d_max_y) + ")\n"
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Displacement, Uz":
                    scalars = self.deformation[:, 2]
                    d_max_z = np.max(np.abs(self.deformation[:, 2]))
                    stitle = "Displacement, Uz (Max. = " + str(d_max_z) + ")\n"
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Displacement, Uxyz":
                    scalars = self.deformation[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    d_max_xyz = np.max(np.abs(scalars))
                    stitle = "Displacement, Uxyz (Max. = " + str(d_max_xyz) + ")\n"
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Rotation, Rx":
                    scalars = self.rotation[:, 2]
                    stitle = (
                        "Rotation, Rx (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Rotation, Ry":
                    scalars = self.rotation[:, 1]
                    stitle = (
                        "Rotation, Ry (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Rotation, Rz":
                    scalars = self.rotation[:, 0]
                    stitle = (
                        "Rotation, Rz (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Rotation, Rxyz":
                    scalars = self.rotation[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Rotation, Rxyz (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Force Reaction, RFx":
                    scalars = self.forcereaction[:, 0]
                    stitle = (
                        "Force Reaction, RFx (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Force Reaction, RFy":
                    scalars = self.forcereaction[:, 1]
                    stitle = (
                        "Force Reaction, RFy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    # stitle = 'Force Reaction, RFy\n'
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Force Reaction, RFz":
                    scalars = self.forcereaction[:, 2]
                    stitle = (
                        "Force Reaction, RFz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Force Reaction, RFxyz":
                    scalars = self.forcereaction[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Force Reaction, RFxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Moment Reaction, RMx":
                    scalars = self.momentreaction[:, 2]
                    stitle = (
                        "Moment Reaction, RMx (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Moment Reaction, RMy":
                    scalars = self.momentreaction[:, 1]
                    stitle = (
                        "Moment Reaction, RMy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    # stitle = 'Moment Reaction, RMx\n'
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Moment Reaction, RMz":
                    scalars = self.momentreaction[:, 0]
                    stitle = (
                        "Moment Reaction, RMz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    # stitle = 'Moment Reaction, RMz\n'
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Moment Reaction, RMxyz":
                    scalars = self.momentreaction[:, :3]
                    stitle = (
                        "Moment Reaction, RMxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
            elif self.actionSmooth_View_Wiremesh_undeform.isChecked() == True:
                if node_contour_type == "Displacement, Ux":
                    scalars = self.deformation[:, 0]
                    d_max_x = np.max(np.abs(self.deformation[:, 0]))
                    stitle = "Displacement, Ux (Max. = " + str(d_max_x) + ")\n"
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Displacement, Uy":
                    scalars = self.deformation[:, 1]
                    d_max_y = np.max(np.abs(self.deformation[:, 1]))
                    stitle = "Displacement, Uy (Max. = " + str(d_max_y) + ")\n"
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Displacement, Uz":
                    scalars = self.deformation[:, 2]
                    d_max_z = np.max(np.abs(self.deformation[:, 2]))
                    stitle = "Displacement, Uz (Max. = " + str(d_max_z) + ")\n"
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Displacement, Uxyz":
                    scalars = self.deformation[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    d_max_xyz = np.max(np.abs(scalars))
                    stitle = "Displacement, Uxyz (Max. = " + str(d_max_xyz) + ")\n"
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Rotation, Rx":
                    scalars = self.rotation[:, 2]
                    stitle = (
                        "Rotation, Rx (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                elif node_contour_type == "Rotation, Ry":
                    scalars = self.rotation[:, 1]
                    stitle = (
                        "Rotation, Ry (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Rotation, Rz":
                    scalars = self.rotation[:, 0]
                    stitle = (
                        "Rotation, Rz (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Rotation, Rxyz":
                    scalars = self.rotation[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Rotation, Rxyz (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Force Reaction, RFx":
                    scalars = self.forcereaction[:, 0]
                    stitle = (
                        "Force Reaction, RFx (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Force Reaction, RFy":
                    scalars = self.forcereaction[:, 1]
                    stitle = (
                        "Force Reaction, RFy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    # stitle = 'Force Reaction, RFy\n'
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Force Reaction, RFz":
                    scalars = self.forcereaction[:, 2]
                    stitle = (
                        "Force Reaction, RFz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Force Reaction, RFxyz":
                    scalars = self.forcereaction[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Force Reaction, RFxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Moment Reaction, RMx":
                    scalars = self.momentreaction[:, 2]
                    stitle = (
                        "Moment Reaction, RMx (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Moment Reaction, RMy":
                    scalars = self.momentreaction[:, 1]
                    stitle = (
                        "Moment Reaction, RMy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    # stitle = 'Moment Reaction, RMx\n'
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Moment Reaction, RMz":
                    scalars = self.momentreaction[:, 0]
                    stitle = (
                        "Moment Reaction, RMz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    # stitle = 'Moment Reaction, RMz\n'
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
                elif node_contour_type == "Moment Reaction, RMxyz":
                    scalars = self.momentreaction[:, :3]
                    stitle = (
                        "Moment Reaction, RMxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords,
                        scalars,
                        stitle,
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "wireframe",
                        NodeCoords(self.fileName),
                        None,
                        None,
                    )
            if self.step_dynamic > 0:
                for i in range(self.step_dynamic):
                    # add items to as dynamic steps in Step Num. Combobox
                    self.cb_steps_dynamic.addItem(str(i))
            if self.actionView_Support.isChecked() == True:
                support_disp(self.fileName, self.p, self.dispNodeCoords)

        except:
            QMessageBox.critical(self, "Error", "Check the recorders options")

    def DispModal(self):
        try:
            self.dispNodeCoords = None
            self.btn_apply_static.setChecked(False)
            self.btn_apply_dynamic.setChecked(False)
            mode_file = self.cb_numNodes.currentText()
            scalefactor = float(self.tb_sef_scale_factor.text())
            # read period.out file
            period_file = os.path.join(self.result_directory, "Periods.out")
            outperiodFile = OpenSeesOutputRead(period_file)
            nodes = node(main.fileName)[:, 1].astype(int)
            # all_nodes = nodes.reshape((-1, 1))
            all_nodes = np.sort(nodes).reshape((-1, 1))
            nodes_inex = []
            for i in range(len(nodes)):
                nodes_in = list(all_nodes).index(nodes[i])
                # list(vowels).index(5)
                nodes_inex.append(nodes_in)

            for i in range(int(numModes)):
                if mode_file == "Mode_" + str(i + 1):
                    mode_filename = os.path.join(
                        self.result_directory, "Mode_" + str(i + 1) + ".out"
                    )
                    outdispModalFile = OpenSeesOutputRead(mode_filename)
                    step = len(outdispModalFile[:, 1])
                    if ndm_v(self.fileName) == 3:
                        self.deformation_modal = outdispModalFile[
                            int(step) - 1, 0:
                        ].reshape(-1, 3)
                        self.deformation_modal_s = []
                        for j in range(len(nodes)):
                            self.deformation_modal_1 = self.deformation_modal[
                                nodes_inex[j]
                            ]
                            self.deformation_modal_s.append(self.deformation_modal_1)
                        self.deformation_modal_f = np.vstack(self.deformation_modal_s)
                    if ndm_v(self.fileName) == 2:
                        deformation_modal_xy = outdispModalFile[
                            int(step) - 1, 0:
                        ].reshape(-1, 2)
                        z_def = np.repeat(0, len(deformation_modal_xy[:, 0]))
                        self.deformation_modal_f = np.column_stack(
                            [deformation_modal_xy, z_def]
                        )
                    self.dispNodeCoords_Modal = NodeCoords(self.fileName) + (
                        scalefactor * self.deformation_modal_f
                    )
                    self.p.clear()
                    node_contour_type = self.cb_node_contour_modal.currentText()
                    if self.actionMesh_View_2.isChecked() == True:
                        if node_contour_type == "Displacement, Ux":
                            scalars = self.deformation_modal_f[:, 0]
                            stitle = (
                                "Mode_"
                                + str(i + 1)
                                + "[Fr. = "
                                + str(float(np.round(1 / outperiodFile[i], 3)))
                                + " Hz,"
                                + " T. = "
                                + str(float(np.round(outperiodFile[i], 5)))
                                + " s]"
                                + "; "
                                + "Disp., Ux\n"
                            )
                            plotter(
                                self.p,
                                self.fileName,
                                "mesh_view",
                                self.dispNodeCoords_Modal,
                                scalars,
                                stitle,
                            )
                        if node_contour_type == "Displacement, Uy":
                            scalars = self.deformation_modal_f[:, 1]
                            stitle = (
                                "Mode_"
                                + str(i + 1)
                                + "[Freq. = "
                                + str(float(np.round(1 / outperiodFile[i], 3)))
                                + " Hz,"
                                + " T. = "
                                + str(float(np.round(outperiodFile[i], 5)))
                                + " s]"
                                + "; "
                                + "Disp., Uy\n"
                            )
                            plotter(
                                self.p,
                                self.fileName,
                                "mesh_view",
                                self.dispNodeCoords_Modal,
                                scalars,
                                stitle,
                            )
                        if node_contour_type == "Displacement, Uz":
                            scalars = self.deformation_modal_f[:, 2]
                            stitle = (
                                "Mode_"
                                + str(i + 1)
                                + "[Freq. "
                                + str(i + 1)
                                + "[Freq. = "
                                + str(float(np.round(1 / outperiodFile[i], 3)))
                                + " Hz,"
                                + " T. = "
                                + str(float(np.round(outperiodFile[i], 5)))
                                + " s]"
                                + "; "
                                + "Disp., Uz\n"
                            )
                            plotter(
                                self.p,
                                self.fileName,
                                "mesh_view",
                                self.dispNodeCoords_Modal,
                                scalars,
                                stitle,
                            )
                        if node_contour_type == "Displacement, Uxyz":
                            scalars = self.deformation_modal_f[:, :3]
                            scalars = (scalars * scalars).sum(1) ** 0.5
                            stitle = (
                                "Mode_"
                                + str(i + 1)
                                + "[Freq. = "
                                + str(float(np.round(1 / outperiodFile[i], 3)))
                                + " Hz,"
                                + " T. = "
                                + str(float(np.round(outperiodFile[i], 5)))
                                + " s]"
                                + "; "
                                + "Disp., Uxyz\n"
                            )
                            plotter(
                                self.p,
                                self.fileName,
                                "mesh_view",
                                self.dispNodeCoords_Modal,
                                scalars,
                                stitle,
                            )
                    if self.actionSmooth_View_2.isChecked() == True:
                        if node_contour_type == "Displacement, Ux":
                            scalars = self.deformation_modal_f[:, 0]
                            stitle = (
                                "Mode_"
                                + str(i + 1)
                                + "[Freq. = "
                                + str(float(np.round(1 / outperiodFile[i], 3)))
                                + " Hz,"
                                + " T. = "
                                + str(float(np.round(outperiodFile[i], 5)))
                                + " s]"
                                + "; "
                                + "Disp., Ux\n"
                            )
                            plotter(
                                self.p,
                                self.fileName,
                                "smooth_view",
                                self.dispNodeCoords_Modal,
                                scalars,
                                stitle,
                            )
                        if node_contour_type == "Displacement, Uy":
                            scalars = self.deformation_modal_f[:, 1]
                            stitle = (
                                "Mode_"
                                + str(i + 1)
                                + "[Freq. = "
                                + str(float(np.round(1 / outperiodFile[i], 3)))
                                + " Hz,"
                                + " T. = "
                                + str(float(np.round(outperiodFile[i], 5)))
                                + " s]"
                                + "; "
                                + "Disp., Ux\n"
                            )
                            plotter(
                                self.p,
                                self.fileName,
                                "smooth_view",
                                self.dispNodeCoords_Modal,
                                scalars,
                                stitle,
                            )
                        if node_contour_type == "Displacement, Uz":
                            scalars = self.deformation_modal_f[:, 2]
                            stitle = (
                                "Mode_"
                                + str(i + 1)
                                + "[Freq. "
                                + str(i + 1)
                                + "[Freq. = "
                                + str(float(np.round(1 / outperiodFile[i], 3)))
                                + " Hz,"
                                + " T. = "
                                + str(float(np.round(outperiodFile[i], 5)))
                                + " s]"
                                + "; "
                                + "Disp., Uz\n"
                            )
                            plotter(
                                self.p,
                                self.fileName,
                                "smooth_view",
                                self.dispNodeCoords_Modal,
                                scalars,
                                stitle,
                            )
                        if node_contour_type == "Displacement, Uxyz":
                            scalars = self.deformation_modal_f[:, :3]
                            scalars = (scalars * scalars).sum(1) ** 0.5
                            stitle = (
                                "Mode_"
                                + str(i + 1)
                                + "[Freq. = "
                                + str(float(np.round(1 / outperiodFile[i], 3)))
                                + " Hz,"
                                + " T. = "
                                + str(float(np.round(outperiodFile[i], 5)))
                                + " s]"
                                + "; "
                                + "Disp., Uxyz\n"
                            )
                            plotter(
                                self.p,
                                self.fileName,
                                "smooth_view",
                                self.dispNodeCoords_Modal,
                                scalars,
                                stitle,
                            )

                    if self.actionMesh_View_Wiremesh_undeform.isChecked() == True:
                        if node_contour_type == "Displacement, Ux":
                            scalars = self.deformation_modal_f[:, 0]
                            stitle = (
                                "Mode_"
                                + str(i + 1)
                                + "[Fr. = "
                                + str(float(np.round(1 / outperiodFile[i], 3)))
                                + " Hz,"
                                + " T. = "
                                + str(float(np.round(outperiodFile[i], 5)))
                                + " s]"
                                + "; "
                                + "Disp., Ux\n"
                            )
                            plotter(
                                self.p,
                                self.fileName,
                                "mesh_view",
                                self.dispNodeCoords_Modal,
                                scalars,
                                stitle,
                            )
                        if node_contour_type == "Displacement, Ux":
                            scalars = self.deformation_modal_f[:, 1]
                            stitle = (
                                "Mode_"
                                + str(i + 1)
                                + "[Freq. = "
                                + str(float(np.round(1 / outperiodFile[i], 3)))
                                + " Hz,"
                                + " T. = "
                                + str(float(np.round(outperiodFile[i], 5)))
                                + " s]"
                                + "; "
                                + "Disp., Uy\n"
                            )
                            plotter(
                                self.p,
                                self.fileName,
                                "mesh_view",
                                self.dispNodeCoords_Modal,
                                scalars,
                                stitle,
                            )
                        if node_contour_type == "Displacement, Uz":
                            scalars = self.deformation_modal_f[:, 2]
                            stitle = (
                                "Mode_"
                                + str(i + 1)
                                + "[Freq. "
                                + str(i + 1)
                                + "[Freq. = "
                                + str(float(np.round(1 / outperiodFile[i], 3)))
                                + " Hz,"
                                + " T. = "
                                + str(float(np.round(outperiodFile[i], 5)))
                                + " s]"
                                + "; "
                                + "Disp., Uz\n"
                            )
                            plotter(
                                self.p,
                                self.fileName,
                                "mesh_view",
                                self.dispNodeCoords_Modal,
                                scalars,
                                stitle,
                            )
                        if node_contour_type == "Displacement, Uxyz":
                            scalars = self.deformation_modal_f[:, :3]
                            scalars = (scalars * scalars).sum(1) ** 0.5
                            stitle = (
                                "Mode_"
                                + str(i + 1)
                                + "[Freq. = "
                                + str(float(np.round(1 / outperiodFile[i], 3)))
                                + " Hz,"
                                + " T. = "
                                + str(float(np.round(outperiodFile[i], 5)))
                                + " s]"
                                + "; "
                                + "Disp., Uxyz\n"
                            )
                            plotter(
                                self.p,
                                self.fileName,
                                "mesh_view",
                                self.dispNodeCoords_Modal,
                                scalars,
                                stitle,
                            )
                        plotter(
                            self.p,
                            self.fileName,
                            "wireframe",
                            NodeCoords(self.fileName),
                            None,
                            None,
                        )

                    if self.actionSmooth_View_Wiremesh_undeform.isChecked() == True:
                        if node_contour_type == "Displacement, Ux":
                            scalars = self.deformation_modal_f[:, 0]
                            stitle = (
                                "Mode_"
                                + str(i + 1)
                                + "[Freq. = "
                                + str(float(np.round(1 / outperiodFile[i], 3)))
                                + " Hz,"
                                + " T. = "
                                + str(float(np.round(outperiodFile[i], 5)))
                                + " s]"
                                + "; "
                                + "Disp., Ux\n"
                            )
                            plotter(
                                self.p,
                                self.fileName,
                                "smooth_view",
                                self.dispNodeCoords_Modal,
                                scalars,
                                stitle,
                            )
                        if node_contour_type == "Displacement, Uy":
                            scalars = self.deformation_modal_f[:, 1]
                            stitle = (
                                "Mode_"
                                + str(i + 1)
                                + "[Freq. = "
                                + str(float(np.round(1 / outperiodFile[i], 3)))
                                + " Hz,"
                                + " T. = "
                                + str(float(np.round(outperiodFile[i], 5)))
                                + " s]"
                                + "; "
                                + "Disp., Ux\n"
                            )
                            plotter(
                                self.p,
                                self.fileName,
                                "smooth_view",
                                self.dispNodeCoords_Modal,
                                scalars,
                                stitle,
                            )
                        if node_contour_type == "Displacement, Uz":
                            scalars = self.deformation_modal_f[:, 2]
                            stitle = (
                                "Mode_"
                                + str(i + 1)
                                + "[Freq. "
                                + str(i + 1)
                                + "[Freq. = "
                                + str(float(np.round(1 / outperiodFile[i], 3)))
                                + " Hz,"
                                + " T. = "
                                + str(float(np.round(outperiodFile[i], 5)))
                                + " s]"
                                + "; "
                                + "Disp., Uz\n"
                            )
                            plotter(
                                self.p,
                                self.fileName,
                                "smooth_view",
                                self.dispNodeCoords_Modal,
                                scalars,
                                stitle,
                            )
                        if node_contour_type == "Displacement, Uxyz":
                            scalars = self.deformation_modal_f[:, :3]
                            scalars = (scalars * scalars).sum(1) ** 0.5
                            stitle = (
                                "Mode_"
                                + str(i + 1)
                                + "[Freq. = "
                                + str(float(np.round(1 / outperiodFile[i], 3)))
                                + " Hz,"
                                + " T. = "
                                + str(float(np.round(outperiodFile[i], 5)))
                                + " s]"
                                + "; "
                                + "Disp., Uxyz\n"
                            )
                            plotter(
                                self.p,
                                self.fileName,
                                "smooth_view",
                                self.dispNodeCoords_Modal,
                                scalars,
                                stitle,
                            )
                        plotter(
                            self.p,
                            self.fileName,
                            "wireframe",
                            NodeCoords(self.fileName),
                            None,
                            None,
                        )
            if self.actionView_Support.isChecked() == True:
                # show support
                support_disp(self.fileName, self.p, self.dispNodeCoords_Modal)
        except:
            QMessageBox.critical(self, "Error", "Check the recorders options")

    # function to open help file
    def FeView_Help(self):
        try:
            programName = "Help\FeView_Help.chm"
            sp.Popen([programName])
        except:
            QMessageBox.critical(
                self,
                "Error",
                "Please check FeView_Help.chm file exist or not in the help folder of the installation directory",
            )

    # function to create the close event for the GUI
    def closeEvent(self, event):
        return (
            event.accept()
            if QMessageBox.question(
                self,
                "Close",
                "Want to Exit ?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )
            == QMessageBox.Yes
            else event.ignore()
        )

    # function to save the model as a picture with current background-color
    def savePlot(self):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName_p, _ = QFileDialog.getSaveFileName(
                self, "Save Model as Picture", "", "PNG (*.png)"
            )
            if fileName_p:
                self.currentdir = os.path.dirname(os.path.abspath(fileName_p))
                self.p.screenshot(fileName_p)
        except:
            QMessageBox.critical(self, "Error", "Please check, unknown reason")

    # function to save the model as a picture with white background
    def savePlot_wb(self):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName_p_wb, _ = QFileDialog.getSaveFileName(
                self, "Save Plot as Picture", "", "PNG (*.png)"
            )
            if fileName_p_wb:
                self.currentdir = os.path.dirname(os.path.abspath(fileName_p_wb))
                self.p.screenshot(
                    fileName_p_wb, transparent_background=True, return_img=10
                )
        except:
            QMessageBox.critical(self, "Error", "Please check, unknown reason")

    def calculator(self):
        try:
            programName = "calc.exe"
            sp.Popen([programName])
        except:
            QMessageBox.critical(
                self, "Error", "calc.exe should be available in your system"
            )

    def center(self):  # QDesktopWidget이 없어져서 아래와 같이 수정함.
        try:
            """Center and resize the window."""
            self.showNormal()
            screen = QGuiApplication.primaryScreen().size()
            size = self.geometry()
            self.resize(
                (screen.width() - size.width()) // 1.25,
                (screen.height() - size.height()) // 1.25,
            )
            return self.move(
                (screen.width() - size.width()) / 2,
                (screen.height() - size.height()) / 2,
            )
        except:
            QMessageBox.critical(self, "Error", "Please check, unknown reason")

    def gui_color(self):
        try:
            GUI_color = QColorDialog.getColor()
            if GUI_color.isValid():
                # self.p.set_background(str(GUI_color.name()))
                main.setStyleSheet("background-color: white;")
                main.setStyleSheet("background-color:" + str(GUI_color.name()) + ";")
                main.dockWidget.setStyleSheet(
                    "background-color:" + str(GUI_color.name()) + ";"
                )
                # main.dockWidget1.setStyleSheet("background-color:" + str(GUI_color.name()) + ';')
                main.groupBox.setStyleSheet(
                    "background-color:" + str(GUI_color.name()) + ";"
                )
                main.groupBox_10.setStyleSheet(
                    "background-color:" + str(GUI_color.name()) + ";"
                )
                main.groupBox_2.setStyleSheet(
                    "background-color:" + str(GUI_color.name()) + ";"
                )
                main.groupBox_5.setStyleSheet(
                    "background-color:" + str(GUI_color.name()) + ";"
                )
                main.groupBox_7.setStyleSheet(
                    "background-color:" + str(GUI_color.name()) + ";"
                )

                main.btn_openTCL.setStyleSheet(
                    "background-color:" + str(GUI_color.name()) + ";"
                )
                main.label_3.setStyleSheet(
                    "background-color:" + str(GUI_color.name()) + ";"
                )
                main.sldr_deform_scale.setStyleSheet(
                    "background-color:" + str(GUI_color.name()) + ";"
                )
                main.btn_apply_static.setStyleSheet(
                    "background-color:" + str(GUI_color.name()) + ";"
                )
                main.label.setStyleSheet(
                    "background-color:" + str(GUI_color.name()) + ";"
                )

                main.sldr_deform_scale_modal.setStyleSheet(
                    "background-color:" + str(GUI_color.name()) + ";"
                )
                main.btn_apply_modal.setStyleSheet(
                    "background-color:" + str(GUI_color.name()) + ";"
                )
                main.sldr_deform_scale_dynamic.setStyleSheet(
                    "background-color:" + str(GUI_color.name()) + ";"
                )
                main.btn_apply_dynamic.setStyleSheet(
                    "background-color:" + str(GUI_color.name()) + ";"
                )
                main.label_5.setStyleSheet(
                    "background-color:" + str(GUI_color.name()) + ";"
                )
        except:
            QMessageBox.critical(self, "Error", "Please provide python supported color")

    def Plot_Background_Color(self):
        try:
            plot_background_color = QColorDialog.getColor()
            if plot_background_color.isValid():
                self.p.set_background(str(plot_background_color.name()))
        except:
            QMessageBox.critical(self, "Error", "Please provide python supported color")

    def GUI_Font(self):
        try:
            self.setFont(QFontDialog.getFont(self)[0])
        except:
            QMessageBox.critical(
                self, "Error", "Fonts style should be supported by PyQt5 "
            )

    def DispDynamic(self):
        try:
            self.dispNodeCoords = None
            self.dispNodeCoords_Modal = None
            self.btn_apply_static.setChecked(False)
            self.btn_apply_modal.setChecked(False)
            # global deformation
            scalefactor = float(self.tb_sef_scale_factor.text())
            if self.recorder_disp == 1:
                self.outdispFile = OpenSeesOutputRead(
                    os.path.join(self.result_directory, "Node_displacements.out")
                )
                self.deformation_dynamic = out_response(
                    (os.path.join(self.result_directory, "Node_displacements.out")),
                    (
                        (self.step_statics)
                        + int(self.cb_steps_dynamic.currentText())
                        + 1
                    ),
                    ndm_v(self.fileName),
                    "all",
                )

            self.dispNodeCoords_dynamic = NodeCoords(self.fileName) + (
                scalefactor * self.deformation_dynamic
            )
            if self.recorder_rot == 1:
                self.rotation_dyanamic = out_response(
                    (os.path.join(self.result_directory, "Node_rotations.out")),
                    (
                        (self.step_statics)
                        + int(self.cb_steps_dynamic.currentText())
                        + 1
                    ),
                    ndm_v(self.fileName),
                    "rotation_moment",
                )
                self.outrotFile = OpenSeesOutputRead(
                    os.path.join(self.result_directory, "Node_rotations.out")
                )
            if self.recorder_force == 1:
                self.forcereaction_dynamic = out_response(
                    (os.path.join(self.result_directory, "Node_forceReactions.out")),
                    (
                        (self.step_statics)
                        + int(self.cb_steps_dynamic.currentText())
                        + 1
                    ),
                    ndm_v(self.fileName),
                    "all",
                )
                self.outfreactFile = OpenSeesOutputRead(
                    os.path.join(self.result_directory, "Node_forceReactions.out")
                )
            if self.recorder_moment == 1:
                self.momentreaction_dynamic = out_response(
                    (os.path.join(self.result_directory, "Node_momentReactions.out")),
                    (
                        (self.step_statics)
                        + int(self.cb_steps_dynamic.currentText())
                        + 1
                    ),
                    ndm_v(self.fileName),
                    "rotation_moment",
                )
                self.outmreactFile = OpenSeesOutputRead(
                    os.path.join(self.result_directory, "Node_momentReactions.out")
                )
            if self.recorder_accel == 1:
                self.acc_dynamic = out_response(
                    (os.path.join(self.result_directory, "Node_accelerations.out")),
                    (
                        (self.step_statics)
                        + int(self.cb_steps_dynamic.currentText())
                        + 1
                    ),
                    ndm_v(self.fileName),
                    "all",
                )
                self.outaccFile = OpenSeesOutputRead(
                    os.path.join(self.result_directory, "Node_accelerations.out")
                )
            if self.recorder_vel == 1:
                self.vel_dynamic = out_response(
                    (os.path.join(self.result_directory, "Node_velocities.out")),
                    (
                        (self.step_statics)
                        + int(self.cb_steps_dynamic.currentText())
                        + 1
                    ),
                    ndm_v(self.fileName),
                    "all",
                )
                self.outvelFile = OpenSeesOutputRead(
                    os.path.join(self.result_directory, "Node_velocities.out")
                )

            node_contour_type_dynamic = self.cb_node_contour_dynamic.currentText()
            self.p.clear()
            if self.actionMesh_View_2.isChecked() == True:
                if node_contour_type_dynamic == "Displacement, Ux":
                    scalars = self.deformation_dynamic[:, 0]
                    stitle = (
                        "Displacement, Ux (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Displacement, Uy":
                    scalars = self.deformation_dynamic[:, 1]
                    stitle = (
                        "Displacement, Uy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Displacement, Uz":
                    scalars = self.deformation_dynamic[:, 2]
                    stitle = (
                        "Displacement, Uz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Displacement, Uxyz":
                    scalars = self.deformation_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Displacement, Uxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Rotation, Rx":
                    scalars = self.rotation_dyanamic[:, 0]
                    stitle = (
                        "Rotation, Rx (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Rotation, Ry":
                    scalars = self.rotation_dyanamic[:, 1]
                    stitle = (
                        "Rotation, Ry (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Rotation, Rz":
                    scalars = self.rotation_dyanamic[:, 2]
                    stitle = (
                        "Rotation, Rz (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Rotation, Rxyz":
                    scalars = self.rotation_dyanamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Rotation, Rxyz (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Force Reaction, RFx":
                    scalars = self.forcereaction_dynamic[:, 0]
                    stitle = (
                        "Force Reaction, RFx (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Force Reaction, RFy":
                    scalars = self.forcereaction_dynamic[:, 1]
                    stitle = (
                        "Force Reaction, RFy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Force Reaction, RFz":
                    scalars = self.forcereaction_dynamic[:, 2]
                    stitle = (
                        "Force Reaction, RFz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Force Reaction, RFxyz":
                    scalars = self.forcereaction_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Force Reaction, RFxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Moment Reaction, RMx":
                    scalars = self.momentreaction_dynamic[:, 0]
                    stitle = (
                        "Moment Reaction, RMx (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Moment Reaction, RMy":
                    scalars = self.momentreaction_dynamic[:, 1]
                    stitle = (
                        "Moment Reaction, RMy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Moment Reaction, RMz":
                    scalars = self.momentreaction_dynamic[:, 2]
                    stitle = (
                        "Moment Reaction, RMz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Moment Reaction, RMxyz":
                    scalars = self.momentreaction_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Moment Reaction, RMxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )

                if node_contour_type_dynamic == "Acceleration, Ax":
                    scalars = self.acc_dynamic[:, 0]
                    stitle = (
                        "Acceleration, Ax (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Acceleration, Ay":
                    scalars = self.acc_dynamic[:, 1]
                    stitle = (
                        "Acceleration, Ay (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Acceleration, Az":
                    scalars = self.acc_dynamic[:, 2]
                    stitle = (
                        "Acceleration, Az (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Acceleration, Axyz":
                    scalars = self.acc_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Acceleration, Axyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )

                if node_contour_type_dynamic == "Velocity, Vx":
                    scalars = self.vel_dynamic[:, 0]
                    stitle = (
                        "Velocity, Vx (Max. = " + str(np.max(np.abs(scalars))) + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Velocity, Vy":
                    scalars = self.vel_dynamic[:, 1]
                    stitle = (
                        "Velocity, Vy (Max. = " + str(np.max(np.abs(scalars))) + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Velocity, Vz":
                    scalars = self.vel_dynamic[:, 2]
                    stitle = (
                        "Velocity, Vz (Max. = " + str(np.max(np.abs(scalars))) + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Velocity, Vxyz":
                    scalars = self.vel_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Velocity, Vxyz (Max. = " + str(np.max(np.abs(scalars))) + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )

            elif self.actionSmooth_View_2.isChecked() == True:
                if node_contour_type_dynamic == "Displacement, Ux":
                    scalars = self.deformation_dynamic[:, 0]
                    stitle = (
                        "Displacement, Ux (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Displacement, Uy":
                    scalars = self.deformation_dynamic[:, 1]
                    stitle = (
                        "Displacement, Uy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Displacement, Uz":
                    scalars = self.deformation_dynamic[:, 2]
                    stitle = (
                        "Displacement, Uz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Displacement, Uxyz":
                    scalars = self.deformation_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Displacement, Uxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Rotation, Rx":
                    scalars = self.rotation_dyanamic[:, 0]
                    stitle = (
                        "Rotation, Rx (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Rotation, Ry":
                    scalars = self.rotation_dyanamic[:, 1]
                    stitle = (
                        "Rotation, Ry (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Rotation, Rz":
                    scalars = self.rotation_dyanamic[:, 2]
                    stitle = (
                        "Rotation, Rz (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Rotation, Rxyz":
                    scalars = self.rotation_dyanamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Rotation, Rxyz (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Force Reaction, RFx":
                    scalars = self.forcereaction_dynamic[:, 0]
                    stitle = (
                        "Force Reaction, RFx (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Force Reaction, RFy":
                    scalars = self.forcereaction_dynamic[:, 1]
                    stitle = (
                        "Force Reaction, RFy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Force Reaction, RFz":
                    scalars = self.forcereaction_dynamic[:, 2]
                    stitle = (
                        "Force Reaction, RFz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Force Reaction, RFxyz":
                    scalars = self.forcereaction_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Force Reaction, RFxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Moment Reaction, RMx":
                    scalars = self.momentreaction_dynamic[:, 0]
                    stitle = (
                        "Moment Reaction, RMx (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Moment Reaction, RMy":
                    scalars = self.momentreaction_dynamic[:, 1]
                    stitle = (
                        "Moment Reaction, RMy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Moment Reaction, RMz":
                    scalars = self.momentreaction_dynamic[:, 2]
                    stitle = (
                        "Moment Reaction, RMz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Moment Reaction, RMxyz":
                    scalars = self.momentreaction_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Moment Reaction, RMxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )

                if node_contour_type_dynamic == "Acceleration, Ax":
                    scalars = self.acc_dynamic[:, 0]
                    stitle = (
                        "Acceleration, Ax (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Acceleration, Ay":
                    scalars = self.acc_dynamic[:, 1]
                    stitle = (
                        "Acceleration, Ay (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Acceleration, Az":
                    scalars = self.acc_dynamic[:, 2]
                    stitle = (
                        "Acceleration, Az (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Acceleration, Axyz":
                    scalars = self.acc_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Acceleration, Axyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )

                if node_contour_type_dynamic == "Velocity, Vx":
                    scalars = self.vel_dynamic[:, 0]
                    stitle = (
                        "Velocity, Vx (Max. = " + str(np.max(np.abs(scalars))) + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Velocity, Vy":
                    scalars = self.vel_dynamic[:, 1]
                    stitle = (
                        "Velocity, Vy (Max. = " + str(np.max(np.abs(scalars))) + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Velocity, Vz":
                    scalars = self.vel_dynamic[:, 2]
                    stitle = (
                        "Velocity, Vz (Max. = " + str(np.max(np.abs(scalars))) + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Velocity, Vxyz":
                    scalars = self.vel_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Velocity, Vxyz (Max. = " + str(np.max(np.abs(scalars))) + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )

            elif self.actionMesh_View_Wiremesh_undeform.isChecked() == True:
                if node_contour_type_dynamic == "Displacement, Ux":
                    scalars = self.deformation_dynamic[:, 0]
                    stitle = (
                        "Displacement, Ux (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Displacement, Uy":
                    scalars = self.deformation_dynamic[:, 1]
                    stitle = (
                        "Displacement, Uy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Displacement, Uz":
                    scalars = self.deformation_dynamic[:, 2]
                    stitle = (
                        "Displacement, Uz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Displacement, Uxyz":
                    scalars = self.deformation_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Displacement, Uxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Rotation, Rx":
                    scalars = self.rotation_dyanamic[:, 0]
                    stitle = (
                        "Rotation, Rx (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Rotation, Ry":
                    scalars = self.rotation_dyanamic[:, 1]
                    stitle = (
                        "Rotation, Ry (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Rotation, Rz":
                    scalars = self.rotation_dyanamic[:, 2]
                    stitle = (
                        "Rotation, Rz (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Rotation, Rxyz":
                    scalars = self.rotation_dyanamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Rotation, Rxyz (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Force Reaction, RFx":
                    scalars = self.forcereaction_dynamic[:, 0]
                    stitle = (
                        "Force Reaction, RFx (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Force Reaction, RFy":
                    scalars = self.forcereaction_dynamic[:, 1]
                    stitle = (
                        "Force Reaction, RFy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Force Reaction, RFz":
                    scalars = self.forcereaction_dynamic[:, 2]
                    stitle = (
                        "Force Reaction, RFz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Force Reaction, RFxyz":
                    scalars = self.forcereaction_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Force Reaction, RFxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Moment Reaction, RMx":
                    scalars = self.momentreaction_dynamic[:, 0]
                    stitle = (
                        "Moment Reaction, RMx (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Moment Reaction, RMy":
                    scalars = self.momentreaction_dynamic[:, 1]
                    stitle = (
                        "Moment Reaction, RMy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Moment Reaction, RMz":
                    scalars = self.momentreaction_dynamic[:, 2]
                    stitle = (
                        "Moment Reaction, RMz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Moment Reaction, RMxyz":
                    scalars = self.momentreaction_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Moment Reaction, RMxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Acceleration, Ax":
                    scalars = self.acc_dynamic[:, 0]
                    stitle = (
                        "Acceleration, Ax (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Acceleration, Ay":
                    scalars = self.acc_dynamic[:, 1]
                    stitle = (
                        "Acceleration, Ay (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Acceleration, Az":
                    scalars = self.acc_dynamic[:, 2]
                    stitle = (
                        "Acceleration, Az (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Acceleration, Axyz":
                    scalars = self.acc_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Acceleration, Axyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Velocity, Vx":
                    scalars = self.vel_dynamic[:, 0]
                    stitle = (
                        "Velocity, Vx (Max. = " + str(np.max(np.abs(scalars))) + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Velocity, Vy":
                    scalars = self.vel_dynamic[:, 1]
                    stitle = (
                        "Velocity, Vy (Max. = " + str(np.max(np.abs(scalars))) + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Velocity, Vz":
                    scalars = self.vel_dynamic[:, 2]
                    stitle = (
                        "Velocity, Vz (Max. = " + str(np.max(np.abs(scalars))) + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Velocity, Vxyz":
                    scalars = self.vel_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Velocity, Vxyz (Max. = " + str(np.max(np.abs(scalars))) + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "mesh_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                plotter(
                    self.p,
                    self.fileName,
                    "wireframe",
                    NodeCoords(self.fileName),
                    None,
                    None,
                )

            elif self.actionSmooth_View_Wiremesh_undeform.isChecked() == True:
                if node_contour_type_dynamic == "Displacement, Ux":
                    scalars = self.deformation_dynamic[:, 0]
                    stitle = (
                        "Displacement, Ux (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Displacement, Uy":
                    scalars = self.deformation_dynamic[:, 1]
                    stitle = (
                        "Displacement, Uy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Displacement, Uz":
                    scalars = self.deformation_dynamic[:, 2]
                    stitle = (
                        "Displacement, Uz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Displacement, Uxyz":
                    scalars = self.deformation_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Displacement, Uxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Rotation, Rx":
                    scalars = self.rotation_dyanamic[:, 0]
                    stitle = (
                        "Rotation, Rx (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Rotation, Ry":
                    scalars = self.rotation_dyanamic[:, 1]
                    stitle = (
                        "Rotation, Ry (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Rotation, Rz":
                    scalars = self.rotation_dyanamic[:, 2]
                    stitle = (
                        "Rotation, Rz (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Rotation, Rxyz":
                    scalars = self.rotation_dyanamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Rotation, Rxyz (rad) (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Force Reaction, RFx":
                    scalars = self.forcereaction_dynamic[:, 0]
                    stitle = (
                        "Force Reaction, RFx (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Force Reaction, RFy":
                    scalars = self.forcereaction_dynamic[:, 1]
                    stitle = (
                        "Force Reaction, RFy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Force Reaction, RFz":
                    scalars = self.forcereaction_dynamic[:, 2]
                    stitle = (
                        "Force Reaction, RFz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Force Reaction, RFxyz":
                    scalars = self.forcereaction_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Force Reaction, RFxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Moment Reaction, RMx":
                    scalars = self.momentreaction_dynamic[:, 0]
                    stitle = (
                        "Moment Reaction, RMx (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Moment Reaction, RMy":
                    scalars = self.momentreaction_dynamic[:, 1]
                    stitle = (
                        "Moment Reaction, RMy (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Moment Reaction, RMz":
                    scalars = self.momentreaction_dynamic[:, 2]
                    stitle = (
                        "Moment Reaction, RMz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Moment Reaction, RMxyz":
                    scalars = self.momentreaction_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Moment Reaction, RMxyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Acceleration, Ax":
                    scalars = self.acc_dynamic[:, 0]
                    stitle = (
                        "Acceleration, Ax (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Acceleration, Ay":
                    scalars = self.acc_dynamic[:, 1]
                    stitle = (
                        "Acceleration, Ay (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Acceleration, Az":
                    scalars = self.acc_dynamic[:, 2]
                    stitle = (
                        "Acceleration, Az (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Acceleration, Axyz":
                    scalars = self.acc_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Acceleration, Axyz (Max. = "
                        + str(np.max(np.abs(scalars)))
                        + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Velocity, Vx":
                    scalars = self.vel_dynamic[:, 0]
                    stitle = (
                        "Velocity, Vx (Max. = " + str(np.max(np.abs(scalars))) + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Velocity, Vy":
                    scalars = self.vel_dynamic[:, 1]
                    stitle = (
                        "Velocity, Vy (Max. = " + str(np.max(np.abs(scalars))) + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Velocity, Vz":
                    scalars = self.vel_dynamic[:, 2]
                    stitle = (
                        "Velocity, Vz (Max. = " + str(np.max(np.abs(scalars))) + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                if node_contour_type_dynamic == "Velocity, Vxyz":
                    scalars = self.vel_dynamic[:, :3]
                    scalars = (scalars * scalars).sum(1) ** 0.5
                    stitle = (
                        "Velocity, Vxyz (Max. = " + str(np.max(np.abs(scalars))) + ")\n"
                    )
                    plotter(
                        self.p,
                        self.fileName,
                        "smooth_view",
                        self.dispNodeCoords_dynamic,
                        scalars,
                        stitle,
                    )
                plotter(
                    self.p,
                    self.fileName,
                    "wireframe",
                    NodeCoords(self.fileName),
                    None,
                    None,
                )
            if self.actionView_Support.isChecked() == True:
                # show support
                support_disp(self.fileName, self.p, self.dispNodeCoords_dynamic)
        except:
            QMessageBox.critical(self, "Error", "Check the recorders options")

    # function to open input file with editor
    def edit_TCL(self):
        try:
            programName = "notepad.exe"
            sp.Popen([programName, self.fileName], cwd=self.file_path)
        except:
            QMessageBox.critical(self, "Error", "Please check OpenSees TCL input file")
        # function to open input file with editor

    def runOS(self):
        try:
            import subprocess as sp

            programName = "OpenSees\OpenSees.exe"
            sp.Popen([programName, self.fileName], cwd=self.result_directory)
        except:
            QMessageBox.critical(
                self,
                "Error",
                "Please check TCL input file and also OpenSees.exe (you should have installed 'Active tcl'",
            )

    # function to unchecked another windows view button except for the isometric view
    def iso(self):
        try:
            self.p.view_isometric()
            self.btn_xy_zpluss.setChecked(False)
            self.btn_xy_zminus.setChecked(False)
            self.btn_xz_ypluss.setChecked(False)
            self.btn_xz_yminus.setChecked(False)
            self.btn_yz_xpluss.setChecked(False)
            self.btn_yz_xminus.setChecked(False)
        except:
            QMessageBox.critical(self, "Error", "Please check, unknown reason")

    # function to unchecked another windows view button except for the xy_zpluss view
    def xy_zpluss(self):
        try:
            self.p.view_xy()
            self.btn_iso.setChecked(False)
            self.btn_xy_zminus.setChecked(False)
            self.btn_xz_ypluss.setChecked(False)
            self.btn_xz_yminus.setChecked(False)
            self.btn_yz_xpluss.setChecked(False)
            self.btn_yz_xminus.setChecked(False)
        except:
            QMessageBox.critical(self, "Error", "Please check, unknown reason")

    # function to unchecked another windows view button except for the xy_zminus view
    def xy_zminus(self):
        try:
            self.p.view_xy(negative=True)
            self.btn_iso.setChecked(False)
            self.btn_xy_zpluss.setChecked(False)
            self.btn_xz_ypluss.setChecked(False)
            self.btn_xz_yminus.setChecked(False)
            self.btn_yz_xpluss.setChecked(False)
            self.btn_yz_xminus.setChecked(False)
        except:
            QMessageBox.critical(self, "Error", "Please check, unknown reason")

    # function to unchecked another windows view button except for the xz_ypluss view
    def xz_ypluss(self):
        try:
            self.p.view_xz()
            self.btn_iso.setChecked(False)
            self.btn_xy_zminus.setChecked(False)
            self.btn_xy_zpluss.setChecked(False)
            self.btn_xz_yminus.setChecked(False)
            self.btn_yz_xpluss.setChecked(False)
            self.btn_yz_xminus.setChecked(False)
        except:
            QMessageBox.critical(self, "Error", "Please check, unknown reason")

    # function to unchecked another windows view button except for the xz_yminus view
    def xz_yminus(self):
        try:
            self.p.view_xz(negative=True)
            self.btn_iso.setChecked(False)
            self.btn_xy_zminus.setChecked(False)
            self.btn_xy_zpluss.setChecked(False)
            self.btn_xz_ypluss.setChecked(False)
            self.btn_yz_xpluss.setChecked(False)
            self.btn_yz_xminus.setChecked(False)
        except:
            QMessageBox.critical(self, "Error", "Please check, unknown reason")

    # function to unchecked another windows view button except for the yz_xpluss view
    def yz_xpluss(self):
        try:
            self.p.view_yz()
            self.btn_iso.setChecked(False)
            self.btn_xy_zminus.setChecked(False)
            self.btn_xy_zpluss.setChecked(False)
            self.btn_xz_ypluss.setChecked(False)
            self.btn_xz_yminus.setChecked(False)
            self.btn_yz_xminus.setChecked(False)
        except:
            QMessageBox.critical(self, "Error", "Please check, unknown reason")

    # function to unchecked another windows view button except for the yz_xminus view
    def yz_xminus(self):
        try:
            self.p.view_yz(negative=True)
            self.btn_iso.setChecked(False)
            self.btn_xy_zminus.setChecked(False)
            self.btn_xy_zpluss.setChecked(False)
            self.btn_xz_ypluss.setChecked(False)
            self.btn_xz_yminus.setChecked(False)
            self.btn_yz_xpluss.setChecked(False)
        except:
            QMessageBox.critical(self, "Error", "Please check, unknown reason")

    # function to show node labels
    def nodelebels(self):
        try:
            self.btn_node_cord.setChecked(False)
            self.btn_load.setChecked(False)
            if self.btn_node_label.isChecked() == True:
                try:
                    # NodesLabel considering static displacement coordinates
                    NodesLabel(self.p, self.fileName, self.dispNodeCoords, 1)
                except:
                    pass
                    try:
                        # NodesLabel considering modal displacement coordinates
                        NodesLabel(self.p, self.fileName, self.dispNodeCoords_Modal, 1)
                    except:
                        pass
                        try:
                            # NodesLabel considering dynamic displacement coordinates
                            NodesLabel(
                                self.p, self.fileName, self.dispNodeCoords_dynamic, 1
                            )
                        except:
                            NodesLabel(
                                self.p, self.fileName, NodeCoords(self.fileName), 1
                            )
            if self.btn_node_label.isChecked() == False:
                NodesLabel(self.p, self.fileName, NodeCoords(self.fileName), 0)
        except:
            QMessageBox.critical(self, "Error", "Please check, unknown reason")

    # function to show node labels
    def nodecoordinates(self):
        try:
            self.btn_node_label.setChecked(False)
            self.btn_load.setChecked(False)
            if self.btn_node_cord.isChecked() == True:
                try:
                    dispNodeCoords = NodeCoords(self.fileName) + (self.deformation)
                    NodesCoordinate(
                        self.p, self.dispNodeCoords, np.round(dispNodeCoords, 3), 1
                    )
                except:
                    pass
                    try:
                        dispNodeCoords_Modal = NodeCoords(self.fileName) + (
                            self.deformation_modal
                        )
                        NodesCoordinate(
                            self.p,
                            self.dispNodeCoords_Modal,
                            np.round(dispNodeCoords_Modal, 3),
                            1,
                        )
                    except:
                        pass
                        try:
                            dispNodeCoords_dynamic = NodeCoords(self.fileName) + (
                                self.deformation_dynamic
                            )
                            NodesCoordinate(
                                self.p,
                                self.dispNodeCoords_dynamic,
                                np.round(dispNodeCoords_dynamic, 3),
                                1,
                            )
                        except:
                            NodesCoordinate(
                                self.p,
                                NodeCoords(self.fileName),
                                NodeCoords(self.fileName),
                                1,
                            )
            # if self.btn_node_cord.isChecked() == False:
            #    NodesCoordinate(self.p, self.fileName, NodeCoords(self.fileName), 0)
        except:
            QMessageBox.critical(self, "Error", "Please check, unknown reason")

    # function for value of scale factor
    def sfvalue(self):
        try:
            self.lbl_scale_cactor.setText(str(self.sldr_deform_scale.value()))
            self.lbl_scale_cactor_modal.setText(
                str(self.sldr_deform_scale_modal.value())
            )
            self.lbl_scale_cactor_dynamic.setText(
                str(self.sldr_deform_scale_dynamic.value())
            )
        except:
            QMessageBox.critical(self, "Error", "Please check, unknown reason")

    #
    def res_static(self):
        try:
            dialog = response_static(self)
            self.dialogs.append(dialog)
            dialog.show()
        except:
            QMessageBox.critical(
                self, "Error", "Please apply the satatic analysis first"
            )

    def res_dynamic(self):
        try:
            dialog = response_dynamic(self)
            self.dialogs.append(dialog)
            dialog.show()
        except:
            QMessageBox.critical(
                self, "Error", "Please apply the satatic analysis first"
            )

    def about_feview(self):
        try:
            dialog = about(self)
            self.dialogs.append(dialog)
            dialog.show()
        except:
            QMessageBox.critical(self, "Error", "Unknown error")

    def data_table_static(self):
        try:
            dialog = table_static(self)
            self.dialogs.append(dialog)
            dialog.show()
        except:
            QMessageBox.critical(self, "Error", "Unknown error")

    def data_table_modal(self):
        try:
            dialog = table_modal(self)
            self.dialogs.append(dialog)
            dialog.show()
        except:
            QMessageBox.critical(self, "Error", "Unknown error")

    def load_setting_arrow(self):
        try:
            if main.actionView_load.isChecked() == True:
                dialog = load_setting(self)
                self.dialogs.append(dialog)
                dialog.show()
        except:
            QMessageBox.critical(self, "Error", "Unknown error")

    def data_table_dynamic(self):
        try:
            dialog = table_dynamic(self)
            self.dialogs.append(dialog)
            dialog.show()
        except:
            QMessageBox.critical(self, "Error", "Unknown error")

    def pointload_show(self):
        try:
            self.btn_node_label.setChecked(False)
            self.btn_node_cord.setChecked(False)

            if self.btn_load.isChecked() == True:
                dialog = load_setting_btn(self)
                self.dialogs.append(dialog)
                dialog.show()
        except:
            QMessageBox.critical(self, "Error", "Please check, unknown reason")


class response_static(QtWidgets.QMainWindow, UI_StaticResponseWindows):
    def __init__(self, parent=None):
        super(response_static, self).__init__(parent)
        # uic.loadUi('UI\StaticResponseWindows.ui', self)
        self.setupUi(self)
        self.btn_insert_static.clicked.connect(self.insert_row_static)
        self.btn_add_roe_static.clicked.connect(self.add_row_static)
        self.btn_delet_row_static.clicked.connect(self.delet_row_static)
        self.cb_dt_static.stateChanged.connect(self.dt_static)
        self.cb_multiStatic.stateChanged.connect(self.multi_static)
        self.actionChange_Background_Color.triggered.connect(
            self.plotresponse_static_bg_color
        )
        self.actionLine_Color_g.triggered.connect(self.plotresponse_static_mg_linecolor)
        self.actionSolid.triggered.connect(self.mg_ls_solid)
        self.actionDotted.triggered.connect(self.mg_ls_dotted)
        self.actionDashed.triggered.connect(self.mg_ls_dashed)
        self.actionDashdot.triggered.connect(self.mg_ls_dashdot)
        self.action0_2.triggered.connect(self.mg_lw_0_2)
        self.action0_4.triggered.connect(self.mg_lw_0_4)
        self.action0_6.triggered.connect(self.mg_lw_0_6)
        self.action0_8.triggered.connect(self.mg_lw_0_8)
        self.action1.triggered.connect(self.mg_lw_1)
        self.mb_savedata.triggered.connect(self.savedata_static)

        self.btn_insert_supportnode.clicked.connect(self.insert_row_pushover)
        self.btn_add_roe_pushover.clicked.connect(self.add_row_pushover)
        self.btn_delete_roe_pushover.clicked.connect(self.delet_row_pushover)
        self.apply_pushover.clicked.connect(self.plotresponse_pushover)

        self.actionSave_Pushover_Data.triggered.connect(self.savedata_pushover)

        nodes = node(main.fileName)[:, 1].astype(int)

        if nodes.size > 0:
            for i in range(len(nodes)):
                self.cb_resp_nodenumber.addItem(str(nodes[i]))
                self.cb_pushover_nodenumber.addItem(str(nodes[i]))
        self.apply_repnse.clicked.connect(self.plotresponse_static)

    def savedata_pushover(self):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            datafilename, _ = QFileDialog.getSaveFileName(
                self, "Save Data as Text", "", "Text File (*.txt)"
            )
            if datafilename:
                self.currentdir = os.path.dirname(os.path.abspath(datafilename))
                with open(datafilename, "w") as table:
                    table.write("Result data from static analysis: \n\n")

                    table.write("Node Number: " + str(index_cb + 1) + "\n")
                    if node_component_pushover == "Ux":
                        table.write("Displacement_Ux" + "\t" + "Base Shear_Vx\n")
                    elif node_component_pushover == "Uy":
                        table.write("Displacement_Uy" + "\t" + "Base Shear_Vy\n")
                    elif node_component_pushover == "Uz":
                        table.write("Displacement_Uy" + "\t" + "Base Shear_Vy\n")

                    for row in zip(
                        np.round(res_disp, 6), np.round(base_shear_total, 6)
                    ):
                        for cell in row:
                            table.write(str(cell) + "\t")
                        table.write("\n")
        except:
            QMessageBox.critical(
                self, "Error", "Data not found, please apply for pushover"
            )

    def plotresponse_pushover(self):
        global index_cb, res_disp, base_shear_total, node_component_pushover
        try:
            index_cb = self.cb_pushover_nodenumber.currentIndex()
            intrl_disp_static = np.linspace(
                0, 1, len((main.outdispFile[0 : main.step_statics, 0]))
            )
            node_component_pushover = self.cb_pushover_component.currentText()
            # time_static = (float(self.tb_dt_static.text()))
            # time_series_static = (np.linspace(0, time_static * (len(intrl_disp_static) - 1), len(intrl_disp_static)))
            zero_2d_static = x = np.repeat(0, (len(intrl_disp_static)))

            col_count = self.tbl_pushover_supnode.columnCount()
            row_count = self.tbl_pushover_supnode.rowCount()
            headers = [
                str(self.tbl_pushover_supnode.horizontalHeaderItem(i).text())
                for i in range(col_count)
            ]
            df_list = []
            for row in range(row_count):
                df_list2 = []
                for col in range(col_count):
                    table_item = self.tbl_pushover_supnode.item(row, col)
                    df_list2.append(
                        "" if table_item is None else str(table_item.text())
                    )
                df_list.append(df_list2)

            df = pd.DataFrame(df_list, columns=headers)
            sup_node_pushover = df.values.astype(int)
            base_shear = []
            self.PushoverWidget.canvas_pushover.axes_pushover.clear()
            try:
                self.PushoverWidget.canvas_pushover.axes_pushover.set_facecolor(
                    str(plotresponse_static_bg_color.name())
                )
            except:
                self.PushoverWidget.canvas_pushover.axes_pushover.set_facecolor(
                    "#000000"
                )
            try:
                self.PushoverWidget.canvas_pushover.axes_pushover.grid(
                    True, which="both", color=str(plotresponse_static_mg_color.name())
                )
            except:
                self.PushoverWidget.canvas_pushover.axes_pushover.grid(
                    True, which="both", color="#ffffff"
                )
            try:
                self.PushoverWidget.canvas_pushover.axes_pushover.grid(
                    True, which="both", linestyle=lstyle
                )
            except:
                self.PushoverWidget.canvas_pushover.axes_pushover.grid(
                    True, which="both", linestyle="--"
                )
            try:
                self.PushoverWidget.canvas_pushover.axes_pushover.grid(
                    True, which="both", linewidth=lwidth
                )
            except:
                self.PushoverWidget.canvas_pushover.axes_pushover.grid(
                    True, which="both", linewidth=0.4
                )
            #    #
            if node_component_pushover == "Ux":
                if ndm_v(main.fileName) == 3:
                    res_disp = np.abs(
                        (main.outdispFile[0 : main.step_statics, (3 * index_cb + 1)])
                    )
                elif ndm_v(main.fileName) == 2:
                    res_disp = np.abs(
                        (main.outdispFile[0 : main.step_statics, (2 * index_cb + 1)])
                    )
                for i in range(len(sup_node_pushover)):
                    if ndm_v(main.fileName) == 3:
                        res_baseshear = main.outfreactFile[
                            0 : main.step_statics, (3 * sup_node_pushover[i] - 2)
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_baseshear = main.outfreactFile[
                            0 : main.step_statics, (2 * sup_node_pushover[i] - 1)
                        ]

                    base_shear.append(res_baseshear)
                self.PushoverWidget.canvas_pushover.axes_pushover.set_ylabel(
                    "Base Shear, Vx", fontname="Times New Roman", size=10
                )
                self.PushoverWidget.canvas_pushover.axes_pushover.set_xlabel(
                    "Displacement, Ux", fontname="Times New Roman", size=10
                )
                self.PushoverWidget.canvas_pushover.axes_pushover.set_xlim(
                    xmin=np.min(res_disp), xmax=np.max(res_disp)
                )
            elif node_component_pushover == "Uy":
                if ndm_v(main.fileName) == 3:
                    res_disp = np.abs(
                        (main.outdispFile[0 : main.step_statics, (3 * index_cb + 2)])
                    )
                elif ndm_v(main.fileName) == 2:
                    res_disp = np.abs(
                        (main.outdispFile[0 : main.step_statics, (2 * index_cb + 2)])
                    )
                for i in range(len(sup_node_pushover)):
                    if ndm_v(main.fileName) == 3:
                        res_baseshear = np.abs(
                            (
                                main.outfreactFile[
                                    0 : main.step_statics,
                                    (3 * sup_node_pushover[i] - 1),
                                ]
                            )
                        )
                    elif ndm_v(main.fileName) == 2:
                        res_baseshear = np.abs(
                            (
                                main.outfreactFile[
                                    0 : main.step_statics, (2 * sup_node_pushover[i])
                                ]
                            )
                        )

                    base_shear.append(res_baseshear)
                self.PushoverWidget.canvas_pushover.axes_pushover.set_ylabel(
                    "Base Shear, Vy", fontname="Times New Roman", size=10
                )
                self.PushoverWidget.canvas_pushover.axes_pushover.set_xlabel(
                    "Displacement, Uy", fontname="Times New Roman", size=10
                )
                self.PushoverWidget.canvas_pushover.axes_pushover.set_xlim(
                    xmin=np.min(res_disp), xmax=np.max(res_disp)
                )
            elif node_component_pushover == "Uz":
                if ndm_v(main.fileName) == 3:
                    res_disp = np.abs(
                        (main.outdispFile[0 : main.step_statics, (3 * index_cb + 3)])
                    )
                    self.PushoverWidget.canvas_pushover.axes_pushover.set_xlim(
                        xmin=np.min(res_disp), xmax=np.max(res_disp)
                    )
                elif ndm_v(main.fileName) == 2:
                    res_disp = zero_2d_static
                for i in range(len(sup_node_pushover)):
                    if ndm_v(main.fileName) == 3:
                        res_baseshear = np.abs(
                            (
                                main.outfreactFile[
                                    0 : main.step_statics,
                                    (3 * sup_node_pushover[i] - 1),
                                ]
                            )
                        )
                    elif ndm_v(main.fileName) == 2:
                        res_baseshear = zero_2d_static

                    base_shear.append(res_baseshear)
                self.PushoverWidget.canvas_pushover.axes_pushover.set_ylabel(
                    "Base Shear, Vz", fontname="Times New Roman", size=10
                )
                self.PushoverWidget.canvas_pushover.axes_pushover.set_xlabel(
                    "Displacement, Uz", fontname="Times New Roman", size=10
                )
            self.PushoverWidget.canvas_pushover.axes_pushover.yaxis.offsetText.set_fontsize(
                9
            )
            self.PushoverWidget.canvas_pushover.axes_pushover.yaxis.offsetText.set_fontname(
                "Times New Roman"
            )

            for (
                tick
            ) in self.PushoverWidget.canvas_pushover.axes_pushover.get_xticklabels():
                tick.set_fontname("Times New Roman")
                tick.set_fontsize(9)
            for (
                tick
            ) in self.PushoverWidget.canvas_pushover.axes_pushover.get_yticklabels():
                tick.set_fontname("Times New Roman")
                tick.set_fontsize(9)

            base_shear_t = np.transpose(
                np.reshape(
                    np.ravel(base_shear),
                    (len(sup_node_pushover), len(intrl_disp_static)),
                )
            )

            base_shear_total = []
            for i in range(len(base_shear_t[:, 0])):
                base_shear_total.append(np.abs(np.sum(base_shear_t[i, :])))

            self.PushoverWidget.canvas_pushover.axes_pushover.plot(
                res_disp, base_shear_total, color="r", linewidth=1
            )

            self.PushoverWidget.canvas_pushover.axes_pushover.set_ylim(
                ymin=np.min(base_shear_total), ymax=np.max(base_shear_total)
            )

            mpl.rcParams["savefig.dpi"] = 1000
            self.PushoverWidget.canvas_pushover.draw()
        except:
            QMessageBox.critical(self, "Error", "Please ckeck support node")

    def insert_row_pushover(self):
        for i in range(int(self.tb_supportnode.text())):
            self.tbl_pushover_supnode.insertRow(i)

    def add_row_pushover(self):
        row = self.tbl_pushover_supnode.rowCount()
        self.tbl_pushover_supnode.insertRow(row)

    def delet_row_pushover(self):
        index = self.tbl_pushover_supnode.currentIndex()
        self.tbl_pushover_supnode.removeRow(index.row())

    def insert_row_static(self):
        for i in range(int(self.tb_mnode_static.text())):
            self.tbl_static_mtp.insertRow(i)

    def add_row_static(self):
        row = self.tbl_static_mtp.rowCount()
        self.tbl_static_mtp.insertRow(row)

    def delet_row_static(self):
        index = self.tbl_static_mtp.currentIndex()
        self.tbl_static_mtp.removeRow(index.row())

    def multi_static(self, state):
        if state > 0:
            self.gb_multi_static.setEnabled(True)
            self.gb_sigle_static.setEnabled(False)
        else:
            self.gb_multi_static.setEnabled(False)
            self.gb_sigle_static.setEnabled(True)

    def dt_static(self, state):
        if state > 0:
            self.tb_dt_static.setEnabled(True)
        else:
            self.tb_dt_static.setEnabled(False)

    def plotresponse_static_bg_color(self):
        global plotresponse_static_bg_color
        try:
            plotresponse_static_bg_color = QColorDialog.getColor()
        except:
            QMessageBox.critical(
                self, "Error", "Please provide matplotlib supported color"
            )

    def plotresponse_static_mg_linecolor(self):
        global plotresponse_static_mg_color
        try:
            plotresponse_static_mg_color = QColorDialog.getColor()
        except:
            QMessageBox.critical(
                self, "Error", "Please provide matplotlib supported color"
            )

    def mg_ls_solid(self):
        global lstyle
        lstyle = False
        lstyle = "-"

    def mg_ls_dotted(self):
        global lstyle
        lstyle = False
        lstyle = ":"

    def mg_ls_dashed(self):
        global lstyle
        lstyle = False
        lstyle = "--"

    def mg_ls_dashdot(self):
        global lstyle
        lstyle = False
        lstyle = "-."

    def mg_lw_0_2(self):
        global lwidth
        lwidth = False
        lwidth = 0.2

    def mg_lw_0_4(self):
        global lwidth
        lwidth = False
        lwidth = 0.4

    def mg_lw_0_6(self):
        global lwidth
        lwidth = False
        lwidth = 0.6

    def mg_lw_0_8(self):
        global lwidth
        lwidth = False
        lwidth = 0.8

    def mg_lw_1(self):
        global lwidth
        lwidth = False
        lwidth = 1

    def savedata_static(self):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            datafilename, _ = QFileDialog.getSaveFileName(
                self, "Save Data as Text", "", "Text File (*.txt)"
            )
            if datafilename:
                self.currentdir = os.path.dirname(os.path.abspath(datafilename))
                with open(datafilename, "w") as table:
                    table.write("Result data from static analysis: \n\n")
                    if self.cb_multiStatic.isChecked() == False:
                        table.write("Node Number: " + str(index_cb + 1) + "\n")
                        if self.cb_dt_static.isChecked() == False:
                            if node_component_static == "Ux":
                                table.write("Interval" + "\t" + "Displacement_Ux\n")
                            elif node_component_static == "Uy":
                                table.write("Interval" + "\t" + "Displacement_Uy\n")
                            elif node_component_static == "Uz":
                                table.write("Interval" + "\t" + "Displacement_Uz\n")
                            elif node_component_static == "Rx":
                                table.write("Interval" + "\t" + "Rotation_Rx\n")
                            elif node_component_static == "Ry":
                                table.write("Interval" + "\t" + "Rotation_Ry\n")
                            elif node_component_static == "Rz":
                                table.write("Interval" + "\t" + "Rotation_Rz\n")
                            elif node_component_static == "RFx":
                                table.write("Interval" + "\t" + "Reaction_Force_RFx\n")
                            elif node_component_static == "RFy":
                                table.write("Interval" + "\t" + "Reaction_Force_RFy\n")
                            elif node_component_static == "RFz":
                                table.write("Interval" + "\t" + "Reaction_Force_RFz\n")
                            elif node_component_static == "RMx":
                                table.write("Interval" + "\t" + "Moment_Reaction_RMx\n")
                            elif node_component_static == "RMy":
                                table.write("Interval" + "\t" + "Moment_Reaction_RMy\n")
                            elif node_component_static == "RMz":
                                table.write("Interval" + "\t" + "Moment_Reaction_RMz\n")
                            for row in zip(np.round(intrl_disp_static, 4), res_static):
                                for cell in row:
                                    table.write(str(cell) + "\t")
                                table.write("\n")
                        elif self.cb_dt_static.isChecked() == True:
                            if node_component_static == "Ux":
                                table.write("Time(s)" + "\t" + "Displacement_Ux\n")
                            elif node_component_static == "Uy":
                                table.write("Time(s)" + "\t" + "Displacement_Uy\n")
                            elif node_component_static == "Uz":
                                table.write("Time(s)" + "\t" + "Displacement_Uz\n")
                            elif node_component_static == "Rx":
                                table.write("Time(s)" + "\t" + "Rotation_Rx\n")
                            elif node_component_static == "Ry":
                                table.write("Time(s)" + "\t" + "Rotation_Ry\n")
                            elif node_component_static == "Rz":
                                table.write("Time(s)" + "\t" + "Rotation_Rz\n")
                            elif node_component_static == "RFx":
                                table.write("Time(s)" + "\t" + "Reaction_Force_RFx\n")
                            elif node_component_static == "RFy":
                                table.write("Time(s)" + "\t" + "Reaction_Force_RFy\n")
                            elif node_component_static == "RFz":
                                table.write("Time(s)" + "\t" + "Reaction_Force_RFz\n")
                            elif node_component_static == "RMx":
                                table.write("Time(s)" + "\t" + "Moment_Reaction_RMx\n")
                            elif node_component_static == "RMy":
                                table.write("Time(s)" + "\t" + "Moment_Reaction_RMy\n")
                            elif node_component_static == "RMz":
                                table.write("Time(s)" + "\t" + "Moment_Reaction_RMz\n")
                            for row in zip(time_series_static, res_static):
                                for cell in row:
                                    table.write(str(cell) + "\t")
                                table.write("\n")
                    elif self.cb_multiStatic.isChecked() == True:
                        table.write(
                            "Node Number: "
                            + str(np.transpose(nulti_node_static).ravel())
                            + "\n"
                        )
                        response_multinode_static_t = np.transpose(
                            np.reshape(
                                response_multinode_static,
                                (len(nulti_node_static), len(intrl_disp_static)),
                            )
                        )
                        if self.cb_dt_static.isChecked() == False:
                            if node_component_static == "Ux":
                                table.write("Interval" + "\t" + "Displacement_Ux\n")
                            elif node_component_static == "Uy":
                                table.write("Interval" + "\t" + "Displacement_Uy\n")
                            elif node_component_static == "Uz":
                                table.write("Interval" + "\t" + "Displacement_Uz\n")
                            elif node_component_static == "Rx":
                                table.write("Interval" + "\t" + "Rotation_Rx\n")
                            elif node_component_static == "Ry":
                                table.write("Interval" + "\t" + "Rotation_Ry\n")
                            elif node_component_static == "Rz":
                                table.write("Interval" + "\t" + "Rotation_Rz\n")
                            elif node_component_static == "RFx":
                                table.write("Interval" + "\t" + "Reaction_Force_RFx\n")
                            elif node_component_static == "RFy":
                                table.write("Interval" + "\t" + "Reaction_Force_RFy\n")
                            elif node_component_static == "RFz":
                                table.write("Interval" + "\t" + "Reaction_Force_RFz\n")
                            elif node_component_static == "RMx":
                                table.write("Interval" + "\t" + "Moment_Reaction_RMx\n")
                            elif node_component_static == "RMy":
                                table.write("Interval" + "\t" + "Moment_Reaction_RMy\n")
                            elif node_component_static == "RMz":
                                table.write("Interval" + "\t" + "Moment_Reaction_RMz\n")
                            for row in zip(
                                np.round(intrl_disp_static, 4),
                                response_multinode_static_t,
                            ):
                                for cell in row:
                                    table.write(str(cell) + "\t")
                                table.write("\n")
                        elif self.cb_dt_static.isChecked() == True:
                            if node_component_static == "Ux":
                                table.write("Time(s)" + "\t" + "Displacement_Ux\n")
                            elif node_component_static == "Uy":
                                table.write("Time(s)" + "\t" + "Displacement_Uy\n")
                            elif node_component_static == "Uz":
                                table.write("Time(s)" + "\t" + "Displacement_Uz\n")
                            elif node_component_static == "Rx":
                                table.write("Time(s)" + "\t" + "Rotation_Rx\n")
                            elif node_component_static == "Ry":
                                table.write("Time(s)" + "\t" + "Rotation_Ry\n")
                            elif node_component_static == "Rz":
                                table.write("Time(s)" + "\t" + "Rotation_Rz\n")
                            elif node_component_static == "RFx":
                                table.write("Time(s)" + "\t" + "Reaction_Force_RFx\n")
                            elif node_component_static == "RFy":
                                table.write("Time(s)" + "\t" + "Reaction_Force_RFy\n")
                            elif node_component_static == "RFz":
                                table.write("Time(s)" + "\t" + "Reaction_Force_RFz\n")
                            elif node_component_static == "RMx":
                                table.write("Time(s)" + "\t" + "Moment_Reaction_RMx\n")
                            elif node_component_static == "RMy":
                                table.write("Time(s)" + "\t" + "Moment_Reaction_RMy\n")
                            elif node_component_static == "RMz":
                                table.write("Time(s)" + "\t" + "Moment_Reaction_RMz\n")
                            for row in zip(
                                time_series_static, response_multinode_static_t
                            ):
                                for cell in row:
                                    table.write(str(cell) + "\t")
                                table.write("\n")
        except:
            QMessageBox.critical(
                self, "Error", "Data not found, please apply for response"
            )

    def plotresponse_static(self):
        global intrl_disp_static, time_series_static, res_static, node_component_static, index_cb, response_multinode_static, nulti_node_static
        try:
            index_cb = self.cb_resp_nodenumber.currentIndex()
            intrl_disp_static = np.linspace(
                0, 1, len((main.outdispFile[0 : main.step_statics, 0]))
            )
            node_component_static = self.cb_resp_component.currentText()
            time_static = float(self.tb_dt_static.text())
            time_series_static = np.linspace(
                0, time_static * (len(intrl_disp_static) - 1), len(intrl_disp_static)
            )
            zero_2d_static = x = np.repeat(0, (len(intrl_disp_static)))
            self.PstaticWidget.canvas_pstatic.axes_pstatic.clear()
            try:
                self.PstaticWidget.canvas_pstatic.axes_pstatic.set_facecolor(
                    str(plotresponse_static_bg_color.name())
                )
            except:
                self.PstaticWidget.canvas_pstatic.axes_pstatic.set_facecolor("#000000")
            try:
                self.PstaticWidget.canvas_pstatic.axes_pstatic.grid(
                    True, which="both", color=str(plotresponse_static_mg_color.name())
                )
            except:
                self.PstaticWidget.canvas_pstatic.axes_pstatic.grid(
                    True, which="both", color="#ffffff"
                )
            try:
                self.PstaticWidget.canvas_pstatic.axes_pstatic.grid(
                    True, which="both", linestyle=lstyle
                )
            except:
                self.PstaticWidget.canvas_pstatic.axes_pstatic.grid(
                    True, which="both", linestyle="--"
                )
            try:
                self.PstaticWidget.canvas_pstatic.axes_pstatic.grid(
                    True, which="both", linewidth=lwidth
                )
            except:
                self.PstaticWidget.canvas_pstatic.axes_pstatic.grid(
                    True, which="both", linewidth=0.4
                )
            if self.cb_multiStatic.isChecked() == False:  #
                if node_component_static == "Ux":
                    if ndm_v(main.fileName) == 3:
                        res_static = main.outdispFile[
                            0 : main.step_statics, (3 * index_cb + 1)
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_static = main.outdispFile[
                            0 : main.step_statics, (2 * index_cb + 1)
                        ]
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Displacement, Ux", fontname="Times New Roman", size=10
                    )

                elif node_component_static == "Uy":
                    if ndm_v(main.fileName) == 3:
                        res_static = main.outdispFile[
                            0 : main.step_statics, (3 * index_cb + 2)
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_static = main.outdispFile[
                            0 : main.step_statics, (2 * index_cb + 2)
                        ]
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Displacement, Uy", fontname="Times New Roman", size=10
                    )

                elif node_component_static == "Uz":
                    if ndm_v(main.fileName) == 3:
                        res_static = main.outdispFile[
                            0 : main.step_statics, (3 * index_cb + 3)
                        ]
                    elif ndm_v(main.fileName) == 2:
                        QMessageBox.critical(
                            self, "Error", "This DOF is not available for 2D problem"
                        )
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Displacement, Uz", fontname="Times New Roman", size=10
                    )

                elif node_component_static == "Rx":
                    if ndm_v(main.fileName) == 3:
                        res_static = main.outrotFile[
                            0 : main.step_statics, (3 * index_cb + 1)
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_static = zero_2d_static
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Rotation, Rx", fontname="Times New Roman", size=10
                    )
                elif node_component_static == "Ry":
                    if ndm_v(main.fileName) == 3:
                        res_static = main.outrotFile[
                            0 : main.step_statics, (3 * index_cb + 2)
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_static = zero_2d_static
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Rotation, Ry", fontname="Times New Roman", size=10
                    )
                elif node_component_static == "Rz":
                    if ndm_v(main.fileName) == 3:
                        res_static = main.outrotFile[
                            0 : main.step_statics, (3 * index_cb + 3)
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_static = main.outrotFile[
                            0 : main.step_statics, (index_cb + 1)
                        ]
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Rotation, Rz", fontname="Times New Roman", size=10
                    )
                elif node_component_static == "RFx":
                    if ndm_v(main.fileName) == 3:
                        res_static = main.outfreactFile[
                            0 : main.step_statics, (3 * index_cb + 1)
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_static = main.outfreactFile[
                            0 : main.step_statics, (2 * index_cb + 1)
                        ]
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Force Reaction, RFx", fontname="Times New Roman", size=10
                    )
                elif node_component_static == "RFy":
                    if ndm_v(main.fileName) == 3:
                        res_static = main.outfreactFile[
                            0 : main.step_statics, (3 * index_cb + 2)
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_static = main.outfreactFile[
                            0 : main.step_statics, (2 * index_cb + 2)
                        ]
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Force Reaction, RFy", fontname="Times New Roman", size=10
                    )
                elif node_component_static == "RFz":
                    if ndm_v(main.fileName) == 3:
                        res_static = main.outfreactFile[
                            0 : main.step_statics, (3 * index_cb + 3)
                        ]
                    elif ndm_v(main.fileName) == 2:
                        QMessageBox.critical(
                            self, "Error", "This DOF is not available for 2D problem"
                        )
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Force Reaction, RFz", fontname="Times New Roman", size=10
                    )
                elif node_component_static == "RMx":
                    if ndm_v(main.fileName) == 3:
                        res_static = main.outmreactFile[
                            0 : main.step_statics, (3 * index_cb + 1)
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_static = zero_2d_static
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Moment Reaction, RMx", fontname="Times New Roman", size=10
                    )
                elif node_component_static == "RMy":
                    if ndm_v(main.fileName) == 3:
                        res_static = main.outmreactFile[
                            0 : main.step_statics, (3 * index_cb + 2)
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_static = zero_2d_static
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Moment Reaction, RMy", fontname="Times New Roman", size=10
                    )
                elif node_component_static == "RMz":
                    if ndm_v(main.fileName) == 3:
                        res_static = main.outmreactFile[
                            0 : main.step_statics, (3 * index_cb + 3)
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_static = main.outmreactFile[
                            0 : main.step_statics, (index_cb + 1)
                        ]
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Moment Reaction, RMz", fontname="Times New Roman", size=10
                    )

                if self.cb_dt_static.isChecked() == False:
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_xlabel(
                        "Interval", fontname="Times New Roman", size=10
                    )
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                        intrl_disp_static, res_static, color="r", linewidth=1
                    )
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_xlim(
                        xmin=0, xmax=np.max(intrl_disp_static)
                    )
                elif self.cb_dt_static.isChecked() == True:
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_xlabel(
                        "Time (s)", fontname="Times New Roman", size=10
                    )
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                        time_series_static, res_static, color="r", linewidth=1
                    )
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_xlim(
                        xmin=0, xmax=np.max(time_series_static)
                    )

            elif self.cb_multiStatic.isChecked() == True:
                col_count = self.tbl_static_mtp.columnCount()
                row_count = self.tbl_static_mtp.rowCount()
                headers = [
                    str(self.tbl_static_mtp.horizontalHeaderItem(i).text())
                    for i in range(col_count)
                ]
                df_list = []
                for row in range(row_count):
                    df_list2 = []
                    for col in range(col_count):
                        table_item = self.tbl_static_mtp.item(row, col)
                        df_list2.append(
                            "" if table_item is None else str(table_item.text())
                        )
                    df_list.append(df_list2)

                df = pd.DataFrame(df_list, columns=headers)
                nulti_node_static = df.values.astype(int)
                response_multinode_static = []
                if node_component_static == "Ux":
                    for i in range(len(nulti_node_static)):
                        if ndm_v(main.fileName) == 3:
                            res_static = main.outdispFile[
                                0 : main.step_statics, (3 * nulti_node_static[i] - 2)
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_static = main.outdispFile[
                                0 : main.step_statics, (2 * nulti_node_static[i] - 1)
                            ]
                        if self.cb_dt_static.isChecked() == False:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                intrl_disp_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        elif self.cb_dt_static.isChecked() == True:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                time_series_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        response_multinode_static.append(res_static)
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Displacement, Ux", fontname="Times New Roman", size=10
                    )
                elif node_component_static == "Uy":
                    for i in range(len(nulti_node_static)):
                        if ndm_v(main.fileName) == 3:
                            res_static = main.outdispFile[
                                0 : main.step_statics, (3 * nulti_node_static[i] - 1)
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_static = main.outdispFile[
                                0 : main.step_statics, (2 * nulti_node_static[i])
                            ]
                        if self.cb_dt_static.isChecked() == False:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                intrl_disp_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        elif self.cb_dt_static.isChecked() == True:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                time_series_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        response_multinode_static.append(res_static)
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Displacement, Uy", fontname="Times New Roman", size=10
                    )
                elif node_component_static == "Uz":
                    for i in range(len(nulti_node_static)):
                        if ndm_v(main.fileName) == 3:
                            res_static = main.outdispFile[
                                0 : main.step_statics, (3 * nulti_node_static[i])
                            ]
                        elif ndm_v(main.fileName) == 2:
                            QMessageBox.critical(
                                self,
                                "Error",
                                "This DOF is not available for 2D problem",
                            )
                        if self.cb_dt_static.isChecked() == False:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                intrl_disp_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        elif self.cb_dt_static.isChecked() == True:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                time_series_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        response_multinode_static.append(res_static)
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Displacement, Uz", fontname="Times New Roman", size=10
                    )
                elif node_component_static == "Rx":
                    for i in range(len(nulti_node_static)):
                        if ndm_v(main.fileName) == 3:
                            res_static = main.outrotFile[
                                0 : main.step_statics, (3 * nulti_node_static[i] - 2)
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_static = zero_2d_static
                        if self.cb_dt_static.isChecked() == False:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                intrl_disp_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        elif self.cb_dt_static.isChecked() == True:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                time_series_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        response_multinode_static.append(res_static)
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Rotation, Rx", fontname="Times New Roman", size=10
                    )

                elif node_component_static == "Ry":
                    for i in range(len(nulti_node_static)):
                        if ndm_v(main.fileName) == 3:
                            res_static = main.outrotFile[
                                0 : main.step_statics, (3 * nulti_node_static[i] - 1)
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_static = zero_2d_static
                        if self.cb_dt_static.isChecked() == False:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                intrl_disp_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        elif self.cb_dt_static.isChecked() == True:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                time_series_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        response_multinode_static.append(res_static)
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Rotation, Ry", fontname="Times New Roman", size=10
                    )

                elif node_component_static == "Rz":
                    for i in range(len(nulti_node_static)):
                        if ndm_v(main.fileName) == 3:
                            res_static = main.outrotFile[
                                0 : main.step_statics, (3 * nulti_node_static[i])
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_static = main.outrotFile[
                                0 : main.step_statics, (nulti_node_static[i])
                            ]
                        if self.cb_dt_static.isChecked() == False:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                intrl_disp_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        elif self.cb_dt_static.isChecked() == True:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                time_series_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        response_multinode_static.append(res_static)
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Rotation, Rz", fontname="Times New Roman", size=10
                    )

                elif node_component_static == "RFx":
                    for i in range(len(nulti_node_static)):
                        if ndm_v(main.fileName) == 3:
                            res_static = main.outfreactFile[
                                0 : main.step_statics, (3 * nulti_node_static[i] - 2)
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_static = main.outfreactFile[
                                0 : main.step_statics, (2 * nulti_node_static[i] - 1)
                            ]
                        if self.cb_dt_static.isChecked() == False:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                intrl_disp_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        elif self.cb_dt_static.isChecked() == True:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                time_series_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        response_multinode_static.append(res_static)
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Force Reaction, RFx", fontname="Times New Roman", size=10
                    )

                elif node_component_static == "RFy":
                    for i in range(len(nulti_node_static)):
                        if ndm_v(main.fileName) == 3:
                            res_static = main.outfreactFile[
                                0 : main.step_statics, (3 * nulti_node_static[i] - 1)
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_static = main.outfreactFile[
                                0 : main.step_statics, (2 * nulti_node_static[i])
                            ]
                        if self.cb_dt_static.isChecked() == False:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                intrl_disp_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        elif self.cb_dt_static.isChecked() == True:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                time_series_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        response_multinode_static.append(res_static)
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Force Reaction, RFy", fontname="Times New Roman", size=10
                    )
                elif node_component_static == "RFz":
                    for i in range(len(nulti_node_static)):
                        if ndm_v(main.fileName) == 3:
                            res_static = main.outfreactFile[
                                0 : main.step_statics, (3 * nulti_node_static[i])
                            ]
                        elif ndm_v(main.fileName) == 2:
                            QMessageBox.critical(
                                self,
                                "Error",
                                "This DOF is not available for 2D problem",
                            )
                        if self.cb_dt_static.isChecked() == False:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                intrl_disp_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        elif self.cb_dt_static.isChecked() == True:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                time_series_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        response_multinode_static.append(res_static)
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Force Reaction, RFz", fontname="Times New Roman", size=10
                    )
                elif node_component_static == "RMx":
                    for i in range(len(nulti_node_static)):
                        if ndm_v(main.fileName) == 3:
                            res_static = main.outmreactFile[
                                0 : main.step_statics, (3 * nulti_node_static[i] - 2)
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_static = zero_2d_static
                        if self.cb_dt_static.isChecked() == False:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                intrl_disp_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        elif self.cb_dt_static.isChecked() == True:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                time_series_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        response_multinode_static.append(res_static)
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Moment Reaction, RMx", fontname="Times New Roman", size=10
                    )
                elif node_component_static == "RMy":
                    for i in range(len(nulti_node_static)):
                        if ndm_v(main.fileName) == 3:
                            res_static = main.outmreactFile[
                                0 : main.step_statics, (3 * nulti_node_static[i] - 1)
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_static = zero_2d_static
                        if self.cb_dt_static.isChecked() == False:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                intrl_disp_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        elif self.cb_dt_static.isChecked() == True:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                time_series_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        response_multinode_static.append(res_static)
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Moement Reaction, RMy", fontname="Times New Roman", size=10
                    )
                elif node_component_static == "RMz":
                    for i in range(len(nulti_node_static)):
                        if ndm_v(main.fileName) == 3:
                            res_static = main.outmreactFile[
                                0 : main.step_statics, (3 * nulti_node_static[i])
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_static = main.outmreactFile[
                                0 : main.step_statics, (nulti_node_static[i])
                            ]
                        if self.cb_dt_static.isChecked() == False:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                intrl_disp_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        elif self.cb_dt_static.isChecked() == True:
                            self.PstaticWidget.canvas_pstatic.axes_pstatic.plot(
                                time_series_static,
                                res_static,
                                linewidth=1,
                                label="Node " + str(nulti_node_static[i]),
                            )
                        response_multinode_static.append(res_static)
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_ylabel(
                        "Moment Reaction, RMz", fontname="Times New Roman", size=10
                    )

                if self.cb_dt_static.isChecked() == False:
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_xlabel(
                        "Interval", fontname="Times New Roman", size=10
                    )
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_xlim(
                        xmin=0, xmax=np.max(intrl_disp_static)
                    )
                elif self.cb_dt_static.isChecked() == True:
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_xlabel(
                        "Time (s)", fontname="Times New Roman", size=10
                    )
                    self.PstaticWidget.canvas_pstatic.axes_pstatic.set_xlim(
                        xmin=0, xmax=np.max(time_series_static)
                    )
                legend = self.PstaticWidget.canvas_pstatic.axes_pstatic.legend(
                    fontsize=10, prop={"family": "Times New Roman"}
                )

            self.PstaticWidget.canvas_pstatic.axes_pstatic.yaxis.offsetText.set_fontsize(
                9
            )
            self.PstaticWidget.canvas_pstatic.axes_pstatic.yaxis.offsetText.set_fontname(
                "Times New Roman"
            )

            for (
                tick
            ) in self.PstaticWidget.canvas_pstatic.axes_pstatic.get_xticklabels():
                tick.set_fontname("Times New Roman")
                tick.set_fontsize(9)
            for (
                tick
            ) in self.PstaticWidget.canvas_pstatic.axes_pstatic.get_yticklabels():
                tick.set_fontname("Times New Roman")
                tick.set_fontsize(9)
            mpl.rcParams["savefig.dpi"] = 1000
            self.PstaticWidget.canvas_pstatic.draw()
        except:
            QMessageBox.critical(self, "Error", "Please check, unknown reason")


class response_dynamic(QtWidgets.QMainWindow, UI_DynamicResponseWindows):
    def __init__(self, parent=None):
        super(response_dynamic, self).__init__(parent)
        # uic.loadUi('UI\dynamicResponseWindows.ui', self)
        self.setupUi(self)
        self.btn_insert_dynamic.clicked.connect(self.insert_row_dynamic)
        self.btn_add_roe_dynamic.clicked.connect(self.add_row_dynamic)
        self.btn_delet_row_dynamic.clicked.connect(self.delet_row_dynamic)
        self.cb_dt_dynamic.stateChanged.connect(self.dt_dynamic)
        self.cb_multiDynamic.stateChanged.connect(self.multi_dynamic)

        self.actionChange_Background_Color.triggered.connect(
            self.plotresponse_dynamic_bg_color
        )
        self.actionLine_Color_g.triggered.connect(
            self.plotresponse_dynamic_mg_linecolor
        )
        self.actionSolid.triggered.connect(self.mg_ls_solid)
        self.actionDotted.triggered.connect(self.mg_ls_dotted)
        self.actionDashed.triggered.connect(self.mg_ls_dashed)

        self.actionDashdot.triggered.connect(self.mg_ls_dashdot)
        self.action0_2.triggered.connect(self.mg_lw_0_2)
        self.action0_4.triggered.connect(self.mg_lw_0_4)
        self.action0_6.triggered.connect(self.mg_lw_0_6)
        self.action0_8.triggered.connect(self.mg_lw_0_8)
        self.action1.triggered.connect(self.mg_lw_1)
        self.mb_savedata_timeseries.triggered.connect(self.savedata_timeseries)
        self.actionResponse_Spectra.triggered.connect(self.savedata_rs)

        nodes = node(main.fileName)[:, 1].astype(int)

        if nodes.size > 0:
            for i in range(len(nodes)):
                self.cb_resp_nodenumber.addItem(str(nodes[i]))
                self.cb_resp_nodenumber_rs.addItem(str(nodes[i]))

        self.apply_repnse_dynamic.clicked.connect(self.plotresponse_dynamic)
        self.apply_rs.clicked.connect(self.res_spectra)

    def insert_row_dynamic(self):
        for i in range(int(self.tb_mnode_dynamic.text())):
            self.tbl_dynamic_mtp.insertRow(i)

    def add_row_dynamic(self):
        row = self.tbl_dynamic_mtp.rowCount()
        self.tbl_dynamic_mtp.insertRow(row)

    def delet_row_dynamic(self):
        index = self.tbl_dynamic_mtp.currentIndex()
        self.tbl_dynamic_mtp.removeRow(index.row())

    def multi_dynamic(self, state):
        if state > 0:
            self.gb_multi_dynamic.setEnabled(True)
            self.gb_sigle_dynamic.setEnabled(False)
        else:
            self.gb_multi_dynamic.setEnabled(False)
            self.gb_sigle_dynamic.setEnabled(True)

    def dt_dynamic(self, state):
        if state > 0:
            self.tb_dt_dynamic.setEnabled(True)
        else:
            self.tb_dt_dynamic.setEnabled(False)

    def plotresponse_dynamic_bg_color(self):
        global plotresponse_dynamic_bg_color
        try:
            plotresponse_dynamic_bg_color = QColorDialog.getColor()
        except:
            QMessageBox.critical(
                self, "Error", "Please provide matplotlib supported color"
            )

    def plotresponse_dynamic_mg_linecolor(self):
        global plotresponse_dynamic_mg_color
        try:
            plotresponse_dynamic_mg_color = QColorDialog.getColor()
        except:
            QMessageBox.critical(
                self, "Error", "Please provide matplotlib supported color"
            )

    def mg_ls_solid(self):
        global lstyle
        lstyle = False
        lstyle = "-"

    def mg_ls_dotted(self):
        global lstyle
        lstyle = False
        lstyle = ":"

    def mg_ls_dashed(self):
        global lstyle
        lstyle = False
        lstyle = "--"

    def mg_ls_dashdot(self):
        global lstyle
        lstyle = False
        lstyle = "-."

    def mg_lw_0_2(self):
        global lwidth
        lwidth = False
        lwidth = 0.2

    def mg_lw_0_4(self):
        global lwidth
        lwidth = False
        lwidth = 0.4

    def mg_lw_0_6(self):
        global lwidth
        lwidth = False
        lwidth = 0.6

    def mg_lw_0_8(self):
        global lwidth
        lwidth = False
        lwidth = 0.8

    def mg_lw_1(self):
        global lwidth
        lwidth = False
        lwidth = 1

    def savedata_rs(self):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            datafilename, _ = QFileDialog.getSaveFileName(
                self, "Save Data as Text", "", "Text File (*.txt)"
            )
            if datafilename:
                self.currentdir = os.path.dirname(os.path.abspath(datafilename))
                with open(datafilename, "w") as table:
                    table.write("Result data from Transient analysis: \n\n")
                    if self.cb_multi_rs.isChecked() == False:
                        table.write("Node Number: " + str(index_cb + 1) + "\n\n")
                        if self.rbn_Ax.isChecked() == True:
                            table.write("Component: X" + "\n\n")
                        elif self.rbn_Ay.isChecked() == True:
                            table.write("Component: Y" + "\n\n")
                        elif self.rbn_Az.isChecked() == True:
                            table.write("Component: Z" + "\n\n")
                        if self.rbn__T.isChecked() == True:
                            if self.rbn_PSa.isChecked() == True:
                                table.write(
                                    "Period(s)"
                                    + "\t"
                                    + "Pseudo Spectral Acceleration_PSa\n"
                                )
                            elif self.rbn_PSv.isChecked() == True:
                                table.write(
                                    "Period(s)"
                                    + "\t"
                                    + "Pseudo Spectral Velocity_PSv\n"
                                )
                            elif self.rbn_Sd.isChecked() == True:
                                table.write(
                                    "Period(s)" + "\t" + "Spectral Displacement_Sd\n"
                                )
                        if self.rbn_F.isChecked() == True:
                            if self.rbn_PSa.isChecked() == True:
                                table.write(
                                    "Frequency(Hz)"
                                    + "\t"
                                    + "Pseudo Spectral Acceleration_PSa\n"
                                )
                            elif self.rbn_PSv.isChecked() == True:
                                table.write(
                                    "Frequency(Hz)"
                                    + "\t"
                                    + "Pseudo Spectral Velocity_PSv\n"
                                )
                            elif self.rbn_Sd.isChecked() == True:
                                table.write(
                                    "Frequency(Hz)"
                                    + "\t"
                                    + "Spectral Displacement_Sd\n"
                                )
                        for row in zip(np.round(x_values, 4), y_values):
                            for cell in row:
                                table.write(str(cell) + "\t")
                            table.write("\n")
                    elif self.cb_multi_rs.isChecked() == True:
                        table.write(
                            "Node Number: "
                            + str(np.transpose(nulti_node_dynamic).ravel())
                            + "\n"
                        )
                        response_multinode_dynamic_t = np.transpose(
                            np.reshape(
                                response_multinode_dynamic,
                                (len(nulti_node_dynamic), len(intrl_disp_dynamic)),
                            )
                        )
                        if self.cb_dt_dynamic.isChecked() == False:
                            if node_component_dynamic == "Ax":
                                table.write("Interval" + "\t" + "Acceleration_Ax\n")
        except:
            QMessageBox.critical(
                self, "Error", "Data not found, please apply for response spectra"
            )

    def savedata_timeseries(self):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            datafilename, _ = QFileDialog.getSaveFileName(
                self, "Save Data as Text", "", "Text File (*.txt)"
            )
            if datafilename:
                self.currentdir = os.path.dirname(os.path.abspath(datafilename))
                with open(datafilename, "w") as table:
                    table.write("Result data from Transient analysis: \n\n")
                    if self.cb_multiDynamic.isChecked() == False:
                        table.write("Node Number: " + str(index_cb + 1) + "\n")
                        if self.cb_dt_dynamic.isChecked() == False:
                            if node_component_dynamic == "Ax":
                                table.write("Interval" + "\t" + "Acceleration_Ax\n")
                            elif node_component_dynamic == "Ay":
                                table.write("Interval" + "\t" + "Acceleration_Ay\n")
                            elif node_component_dynamic == "Ay":
                                table.write("Interval" + "\t" + "Acceleration_Ay\n")
                            elif node_component_dynamic == "Vx":
                                table.write("Interval" + "\t" + "Velocity_Vx\n")
                            elif node_component_dynamic == "Vy":
                                table.write("Interval" + "\t" + "Velocity_Vy\n")
                            elif node_component_dynamic == "Vz":
                                table.write("Interval" + "\t" + "Velocity_Vz\n")
                            elif node_component_dynamic == "Ux":
                                table.write("Interval" + "\t" + "Displacement_Ux\n")
                            elif node_component_dynamic == "Uy":
                                table.write("Interval" + "\t" + "Displacement_Uy\n")
                            elif node_component_dynamic == "Uz":
                                table.write("Interval" + "\t" + "Displacement_Uz\n")
                            elif node_component_dynamic == "Rx":
                                table.write("Interval" + "\t" + "Rotation_Rx\n")
                            elif node_component_dynamic == "Ry":
                                table.write("Interval" + "\t" + "Rotation_Ry\n")
                            elif node_component_dynamic == "Rz":
                                table.write("Interval" + "\t" + "Rotation_Rz\n")
                            elif node_component_dynamic == "RFx":
                                table.write("Interval" + "\t" + "Reaction_Force_RFx\n")
                            elif node_component_dynamic == "RFy":
                                table.write("Interval" + "\t" + "Reaction_Force_RFy\n")
                            elif node_component_dynamic == "RFz":
                                table.write("Interval" + "\t" + "Reaction_Force_RFz\n")
                            elif node_component_dynamic == "RMx":
                                table.write("Interval" + "\t" + "Moment_Reaction_RMx\n")
                            elif node_component_dynamic == "RMy":
                                table.write("Interval" + "\t" + "Moment_Reaction_RMy\n")
                            elif node_component_dynamic == "RMz":
                                table.write("Interval" + "\t" + "Moment_Reaction_RMz\n")
                            for row in zip(
                                np.round(intrl_disp_dynamic, 4), res_dynamic
                            ):
                                for cell in row:
                                    table.write(str(cell) + "\t")
                                table.write("\n")
                        elif self.cb_dt_dynamic.isChecked() == True:
                            if node_component_dynamic == "Ax":
                                table.write("Time(s)" + "\t" + "Acceleration_Ax\n")
                            elif node_component_dynamic == "Ay":
                                table.write("Time(s)" + "\t" + "Acceleration_Ay\n")
                            elif node_component_dynamic == "Ay":
                                table.write("Time(s)" + "\t" + "Acceleration_Ay\n")
                            elif node_component_dynamic == "Vx":
                                table.write("Time(s)" + "\t" + "Velocity_Vx\n")
                            elif node_component_dynamic == "Vy":
                                table.write("Time(s)" + "\t" + "Velocity_Vy\n")
                            elif node_component_dynamic == "Vz":
                                table.write("Time(s)" + "\t" + "Velocity_Vz\n")
                            elif node_component_dynamic == "Ux":
                                table.write("Time(s)" + "\t" + "Displacement_Ux\n")
                            elif node_component_dynamic == "Uy":
                                table.write("Time(s)" + "\t" + "Displacement_Uy\n")
                            elif node_component_dynamic == "Uz":
                                table.write("Time(s)" + "\t" + "Displacement_Uz\n")
                            elif node_component_dynamic == "Rx":
                                table.write("Time(s)" + "\t" + "Rotation_Rx\n")
                            elif node_component_dynamic == "Ry":
                                table.write("Time(s)" + "\t" + "Rotation_Ry\n")
                            elif node_component_dynamic == "Rz":
                                table.write("Time(s)" + "\t" + "Rotation_Rz\n")
                            elif node_component_dynamic == "RFx":
                                table.write("Time(s)" + "\t" + "Reaction_Force_RFx\n")
                            elif node_component_dynamic == "RFy":
                                table.write("Time(s)" + "\t" + "Reaction_Force_RFy\n")
                            elif node_component_dynamic == "RFz":
                                table.write("Time(s)" + "\t" + "Reaction_Force_RFz\n")
                            elif node_component_dynamic == "RMx":
                                table.write("Time(s)" + "\t" + "Moment_Reaction_RMx\n")
                            elif node_component_dynamic == "RMy":
                                table.write("Time(s)" + "\t" + "Moment_Reaction_RMy\n")
                            elif node_component_dynamic == "RMz":
                                table.write("Time(s)" + "\t" + "Moment_Reaction_RMz\n")
                            for row in zip(
                                np.round(time_series_dynamic, 4), res_dynamic
                            ):
                                for cell in row:
                                    table.write(str(cell) + "\t")
                                table.write("\n")
                    elif self.cb_multiDynamic.isChecked() == True:
                        table.write(
                            "Node Number: "
                            + str(np.transpose(nulti_node_dynamic).ravel())
                            + "\n"
                        )
                        response_multinode_dynamic_t = np.transpose(
                            np.reshape(
                                response_multinode_dynamic,
                                (len(nulti_node_dynamic), len(intrl_disp_dynamic)),
                            )
                        )
                        if self.cb_dt_dynamic.isChecked() == False:
                            if node_component_dynamic == "Ax":
                                table.write("Interval" + "\t" + "Acceleration_Ax\n")
                            elif node_component_dynamic == "Ay":
                                table.write("Interval" + "\t" + "Acceleration_Ay\n")
                            elif node_component_dynamic == "Ay":
                                table.write("Interval" + "\t" + "Acceleration_Ay\n")
                            elif node_component_dynamic == "Vx":
                                table.write("Interval" + "\t" + "Velocity_Vx\n")
                            elif node_component_dynamic == "Vy":
                                table.write("Interval" + "\t" + "Velocity_Vy\n")
                            elif node_component_dynamic == "Vz":
                                table.write("Interval" + "\t" + "Velocity_Vz\n")
                            elif node_component_dynamic == "Ux":
                                table.write("Interval" + "\t" + "Displacement_Ux\n")
                            elif node_component_dynamic == "Uy":
                                table.write("Interval" + "\t" + "Displacement_Uy\n")
                            elif node_component_dynamic == "Uz":
                                table.write("Interval" + "\t" + "Displacement_Uz\n")
                            elif node_component_dynamic == "Rx":
                                table.write("Interval" + "\t" + "Rotation_Rx\n")
                            elif node_component_dynamic == "Ry":
                                table.write("Interval" + "\t" + "Rotation_Ry\n")
                            elif node_component_dynamic == "Rz":
                                table.write("Interval" + "\t" + "Rotation_Rz\n")
                            elif node_component_dynamic == "RFx":
                                table.write("Interval" + "\t" + "Reaction_Force_RFx\n")
                            elif node_component_dynamic == "RFy":
                                table.write("Interval" + "\t" + "Reaction_Force_RFy\n")
                            elif node_component_dynamic == "RFz":
                                table.write("Interval" + "\t" + "Reaction_Force_RFz\n")
                            elif node_component_dynamic == "RMx":
                                table.write("Interval" + "\t" + "Moment_Reaction_RMx\n")
                            elif node_component_dynamic == "RMy":
                                table.write("Interval" + "\t" + "Moment_Reaction_RMy\n")
                            elif node_component_dynamic == "RMz":
                                table.write("Interval" + "\t" + "Moment_Reaction_RMz\n")
                            for row in zip(
                                np.round(intrl_disp_dynamic, 4),
                                response_multinode_dynamic_t,
                            ):
                                for cell in row:
                                    table.write(str(cell) + "\t")
                                table.write("\n")
                        elif self.cb_dt_dynamic.isChecked() == True:
                            if node_component_dynamic == "Ax":
                                table.write("Time(s)" + "\t" + "Acceleration_Ax\n")
                            elif node_component_dynamic == "Ay":
                                table.write("Time(s)" + "\t" + "Acceleration_Ay\n")
                            elif node_component_dynamic == "Ay":
                                table.write("Time(s)" + "\t" + "Acceleration_Ay\n")
                            elif node_component_dynamic == "Vx":
                                table.write("Time(s)" + "\t" + "Velocity_Vx\n")
                            elif node_component_dynamic == "Vy":
                                table.write("Time(s)" + "\t" + "Velocity_Vy\n")
                            elif node_component_dynamic == "Vz":
                                table.write("Time(s)" + "\t" + "Velocity_Vz\n")
                            elif node_component_static == "Ux":
                                table.write("Time(s)" + "\t" + "Displacement_Ux\n")
                            elif node_component_static == "Uy":
                                table.write("Time(s)" + "\t" + "Displacement_Uy\n")
                            elif node_component_static == "Uz":
                                table.write("Time(s)" + "\t" + "Displacement_Uz\n")
                            elif node_component_static == "Rx":
                                table.write("Time(s)" + "\t" + "Rotation_Rx\n")
                            elif node_component_static == "Ry":
                                table.write("Time(s)" + "\t" + "Rotation_Ry\n")
                            elif node_component_static == "Rz":
                                table.write("Time(s)" + "\t" + "Rotation_Rz\n")
                            elif node_component_static == "RFx":
                                table.write("Time(s)" + "\t" + "Reaction_Force_RFx\n")
                            elif node_component_static == "RFy":
                                table.write("Time(s)" + "\t" + "Reaction_Force_RFy\n")
                            elif node_component_static == "RFz":
                                table.write("Time(s)" + "\t" + "Reaction_Force_RFz\n")
                            elif node_component_static == "RMx":
                                table.write("Time(s)" + "\t" + "Moment_Reaction_RMx\n")
                            elif node_component_static == "RMy":
                                table.write("Time(s)" + "\t" + "Moment_Reaction_RMy\n")
                            elif node_component_static == "RMz":
                                table.write("Time(s)" + "\t" + "Moment_Reaction_RMz\n")
                            for row in zip(
                                np.round(time_series_dynamic, 4),
                                response_multinode_dynamic_t,
                            ):
                                for cell in row:
                                    table.write(str(cell) + "\t")
                                table.write("\n")
        except:
            QMessageBox.critical(
                self, "Error", "Data not found, please apply for transient analysis"
            )

    #
    def plotresponse_dynamic(self):
        global intrl_disp_dynamic, time_series_dynamic, res_dynamic, node_component_dynamic, index_cb, response_multinode_dynamic, nulti_node_dynamic
        try:
            index_cb = self.cb_resp_nodenumber.currentIndex()
            intrl_disp_dynamic = np.linspace(
                0,
                (len(main.outdispFile[:, 1]) - main.step_statics - 1),
                (len(main.outdispFile[:, 1]) - main.step_statics),
            )
            node_component_dynamic = self.cb_resp_component.currentText()
            time_dynamic = float(self.tb_dt_dynamic.text())
            time_series_dynamic = np.linspace(
                0, time_dynamic * (len(intrl_disp_dynamic) - 1), len(intrl_disp_dynamic)
            )
            zero_2d_dynamic = np.repeat(0, (len(intrl_disp_dynamic)))

            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.clear()
            try:
                self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_facecolor(
                    str(plotresponse_dynamic_bg_color.name())
                )
            except:
                self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_facecolor(
                    "#000000"
                )
            try:
                self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.grid(
                    True, which="both", color=str(plotresponse_dynamic_mg_color.name())
                )
            except:
                self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.grid(
                    True, which="both", color="#ffffff"
                )
            try:
                self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.grid(
                    True, which="both", linestyle=lstyle
                )
            except:
                self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.grid(
                    True, which="both", linestyle="--"
                )
            try:
                self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.grid(
                    True, which="both", linewidth=lwidth
                )
            except:
                self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.grid(
                    True, which="both", linewidth=0.4
                )
            if self.cb_multiDynamic.isChecked() == False:  #
                if node_component_dynamic == "Ax":
                    if ndm_v(main.fileName) == 3:
                        res_dynamic = main.outaccFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (3 * index_cb + 1),
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_dynamic = main.outaccFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (2 * index_cb + 1),
                        ]
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Acceleration, Ax", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Ay":
                    if ndm_v(main.fileName) == 3:
                        res_dynamic = main.outaccFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (3 * index_cb + 2),
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_dynamic = main.outaccFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (2 * index_cb + 2),
                        ]
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Acceleration, Ay", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Az":
                    if ndm_v(main.fileName) == 3:
                        res_dynamic = main.outaccFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (3 * index_cb + 3),
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_dynamic = zero_2d_dynamic
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Acceleration, Az", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Vx":
                    if ndm_v(main.fileName) == 3:
                        res_dynamic = main.outvelFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (3 * index_cb + 1),
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_dynamic = main.outvelFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (2 * index_cb + 1),
                        ]
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Velocity, Vx", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Vy":
                    if ndm_v(main.fileName) == 3:
                        res_dynamic = main.outvelFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (3 * index_cb + 2),
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_dynamic = main.outvelFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (2 * index_cb + 2),
                        ]
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Velocity, Vy", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Vz":
                    if ndm_v(main.fileName) == 3:
                        res_dynamic = main.outvelFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (3 * index_cb + 3),
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_dynamic = zero_2d_dynamic
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Velocity, Vz", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Ux":
                    if ndm_v(main.fileName) == 3:
                        res_dynamic = main.outdispFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (3 * index_cb + 1),
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_dynamic = main.outdispFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (2 * index_cb + 1),
                        ]
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Displacement, Dx", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Uy":
                    if ndm_v(main.fileName) == 3:
                        res_dynamic = main.outdispFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (3 * index_cb + 2),
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_dynamic = main.outdispFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (2 * index_cb + 2),
                        ]
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Displacement, Dy", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Uz":
                    if ndm_v(main.fileName) == 3:
                        res_dynamic = main.outdispFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (3 * index_cb + 3),
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_dynamic = zero_2d_dynamic
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Displacement, Dz", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Rx":
                    if ndm_v(main.fileName) == 3:
                        res_dynamic = main.outrotFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (3 * index_cb + 1),
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_dynamic = zero_2d_dynamic
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Rotation, Rx", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Ry":
                    if ndm_v(main.fileName) == 3:
                        res_dynamic = main.outrotFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (3 * index_cb + 2),
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_dynamic = zero_2d_dynamic
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Rotation, Ry", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Rz":
                    if ndm_v(main.fileName) == 3:
                        res_dynamic = main.outrotFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (3 * index_cb + 3),
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_dynamic = main.outrotFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (index_cb + 1),
                        ]
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Rotation, Rz", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "RFx":
                    if ndm_v(main.fileName) == 3:
                        res_dynamic = main.outfreactFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (3 * index_cb + 1),
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_dynamic = main.outfreactFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (2 * index_cb + 1),
                        ]
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Force Rotation, RFx", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "RFy":
                    if ndm_v(main.fileName) == 3:
                        res_dynamic = main.outfreactFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (3 * index_cb + 2),
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_dynamic = main.outfreactFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (2 * index_cb + 2),
                        ]
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Force Rotation, RFy", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "RFz":
                    if ndm_v(main.fileName) == 3:
                        res_dynamic = main.outfreactFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (3 * index_cb + 3),
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_dynamic = zero_2d_dynamic
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Force Rotation, RFz", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "RMx":
                    if ndm_v(main.fileName) == 3:
                        res_dynamic = main.outmreactFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (3 * index_cb + 1),
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_dynamic = zero_2d_dynamic
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Moment Rotation, RFx", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "RMy":
                    if ndm_v(main.fileName) == 3:
                        res_dynamic = main.outmreactFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (3 * index_cb + 2),
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_dynamic = zero_2d_dynamic
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Moment Rotation, RFx", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "RMz":
                    if ndm_v(main.fileName) == 3:
                        res_dynamic = main.outmreactFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (3 * index_cb + 3),
                        ]
                    elif ndm_v(main.fileName) == 2:
                        res_dynamic = main.outmreactFile[
                            main.step_statics : len(main.outdispFile[:, 1]),
                            (index_cb + 1),
                        ]
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Moment Rotation, RFx", fontname="Times New Roman", size=10
                    )

                if self.cb_dt_dynamic.isChecked() == False:
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_xlabel(
                        "Interval", fontname="Times New Roman", size=10
                    )
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                        intrl_disp_dynamic, res_dynamic, color="r", linewidth=1
                    )
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_xlim(
                        xmin=0, xmax=np.max(intrl_disp_dynamic)
                    )
                elif self.cb_dt_dynamic.isChecked() == True:
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_xlabel(
                        "Time (s)", fontname="Times New Roman", size=10
                    )
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                        time_series_dynamic, res_dynamic, color="r", linewidth=1
                    )
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_xlim(
                        xmin=0, xmax=np.max(time_series_dynamic)
                    )

            elif self.cb_multiDynamic.isChecked() == True:
                col_count = self.tbl_dynamic_mtp.columnCount()
                row_count = self.tbl_dynamic_mtp.rowCount()
                headers = [
                    str(self.tbl_dynamic_mtp.horizontalHeaderItem(i).text())
                    for i in range(col_count)
                ]
                df_list = []
                for row in range(row_count):
                    df_list2 = []
                    for col in range(col_count):
                        table_item = self.tbl_dynamic_mtp.item(row, col)
                        df_list2.append(
                            "" if table_item is None else str(table_item.text())
                        )
                    df_list.append(df_list2)

                df = pd.DataFrame(df_list, columns=headers)
                nulti_node_dynamic = df.values.astype(int)

                if node_component_dynamic == "Ax":
                    response_multinode_dynamic = []
                    for i in range(len(nulti_node_dynamic)):
                        if ndm_v(main.fileName) == 3:
                            res_dynamic = main.outaccFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (3 * nulti_node_dynamic[i] - 2),
                            ]

                        elif ndm_v(main.fileName) == 2:
                            res_dynamic = main.outaccFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (2 * nulti_node_dynamic[i] - 1),
                            ]
                        if self.cb_dt_dynamic.isChecked() == False:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                intrl_disp_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        elif self.cb_dt_dynamic.isChecked() == True:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                time_series_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        response_multinode_dynamic.append(res_dynamic)
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Acceleration, Ax", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Ay":
                    response_multinode_dynamic = []
                    for i in range(len(nulti_node_dynamic)):
                        if ndm_v(main.fileName) == 3:
                            res_dynamic = main.outaccFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (3 * nulti_node_dynamic[i] - 1),
                            ]

                        elif ndm_v(main.fileName) == 2:
                            res_dynamic = main.outaccFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (2 * nulti_node_dynamic[i]),
                            ]
                        if self.cb_dt_dynamic.isChecked() == False:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                intrl_disp_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        elif self.cb_dt_dynamic.isChecked() == True:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                time_series_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        response_multinode_dynamic.append(res_dynamic)
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Acceleration, Ay", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Az":
                    response_multinode_dynamic = []
                    for i in range(len(nulti_node_dynamic)):
                        if ndm_v(main.fileName) == 3:
                            res_dynamic = main.outaccFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (3 * nulti_node_dynamic[i]),
                            ]

                        elif ndm_v(main.fileName) == 2:
                            res_dynamic = zero_2d_dynamic
                        if self.cb_dt_dynamic.isChecked() == False:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                intrl_disp_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        elif self.cb_dt_dynamic.isChecked() == True:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                time_series_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        response_multinode_dynamic.append(res_dynamic)
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Acceleration, Az", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Vx":
                    response_multinode_dynamic = []
                    for i in range(len(nulti_node_dynamic)):
                        if ndm_v(main.fileName) == 3:
                            res_dynamic = main.outvelFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (3 * nulti_node_dynamic[i] - 2),
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_dynamic = main.outvelFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (2 * nulti_node_dynamic[i] - 1),
                            ]
                        if self.cb_dt_dynamic.isChecked() == False:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                intrl_disp_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        elif self.cb_dt_dynamic.isChecked() == True:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                time_series_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        response_multinode_dynamic.append(res_dynamic)
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Velocity, Vx", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Vy":
                    response_multinode_dynamic = []
                    for i in range(len(nulti_node_dynamic)):
                        if ndm_v(main.fileName) == 3:
                            res_dynamic = main.outvelFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (3 * nulti_node_dynamic[i] - 1),
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_dynamic = main.outvelFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (2 * nulti_node_dynamic[i]),
                            ]
                        if self.cb_dt_dynamic.isChecked() == False:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                intrl_disp_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        elif self.cb_dt_dynamic.isChecked() == True:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                time_series_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        response_multinode_dynamic.append(res_dynamic)
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Velocity, Vy", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Vz":
                    response_multinode_dynamic = []
                    for i in range(len(nulti_node_dynamic)):
                        if ndm_v(main.fileName) == 3:
                            res_dynamic = main.outvelFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (3 * nulti_node_dynamic[i]),
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_dynamic = zero_2d_dynamic
                        if self.cb_dt_dynamic.isChecked() == False:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                intrl_disp_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        elif self.cb_dt_dynamic.isChecked() == True:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                time_series_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        response_multinode_dynamic.append(res_dynamic)
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Velocity, Vz", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Ux":
                    response_multinode_dynamic = []
                    for i in range(len(nulti_node_dynamic)):
                        if ndm_v(main.fileName) == 3:
                            res_dynamic = main.outdispFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (3 * nulti_node_dynamic[i] - 2),
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_dynamic = main.outdispFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (2 * nulti_node_dynamic[i] - 1),
                            ]
                        if self.cb_dt_dynamic.isChecked() == False:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                intrl_disp_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        elif self.cb_dt_dynamic.isChecked() == True:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                time_series_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        response_multinode_dynamic.append(res_dynamic)
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Displacement, Dx", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Uy":
                    response_multinode_dynamic = []
                    for i in range(len(nulti_node_dynamic)):
                        if ndm_v(main.fileName) == 3:
                            res_dynamic = main.outdispFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (3 * nulti_node_dynamic[i] - 1),
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_dynamic = main.outdispFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (2 * nulti_node_dynamic[i]),
                            ]
                        if self.cb_dt_dynamic.isChecked() == False:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                intrl_disp_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        elif self.cb_dt_dynamic.isChecked() == True:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                time_series_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        response_multinode_dynamic.append(res_dynamic)
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Displacement, Dy", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Uz":
                    response_multinode_dynamic = []
                    for i in range(len(nulti_node_dynamic)):
                        if ndm_v(main.fileName) == 3:
                            res_dynamic = main.outdispFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (3 * nulti_node_dynamic[i]),
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_dynamic = zero_2d_dynamic
                        if self.cb_dt_dynamic.isChecked() == False:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                intrl_disp_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        elif self.cb_dt_dynamic.isChecked() == True:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                time_series_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        response_multinode_dynamic.append(res_dynamic)
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Displacement, Dz", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Rx":
                    response_multinode_dynamic = []
                    for i in range(len(nulti_node_dynamic)):
                        if ndm_v(main.fileName) == 3:
                            res_dynamic = main.outrotFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (3 * nulti_node_dynamic[i] - 2),
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_dynamic = zero_2d_dynamic
                        if self.cb_dt_dynamic.isChecked() == False:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                intrl_disp_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        elif self.cb_dt_dynamic.isChecked() == True:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                time_series_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        response_multinode_dynamic.append(res_dynamic)
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Rotation, Rx", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Ry":
                    response_multinode_dynamic = []
                    for i in range(len(nulti_node_dynamic)):
                        if ndm_v(main.fileName) == 3:
                            res_dynamic = main.outrotFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (3 * nulti_node_dynamic[i] - 1),
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_dynamic = zero_2d_dynamic
                        if self.cb_dt_dynamic.isChecked() == False:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                intrl_disp_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        elif self.cb_dt_dynamic.isChecked() == True:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                time_series_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        response_multinode_dynamic.append(res_dynamic)
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Rotation, Ry", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "Rz":
                    response_multinode_dynamic = []
                    for i in range(len(nulti_node_dynamic)):
                        if ndm_v(main.fileName) == 3:
                            res_dynamic = main.outrotFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (3 * nulti_node_dynamic[i]),
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_dynamic = main.outrotFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (nulti_node_dynamic[i]),
                            ]
                        if self.cb_dt_dynamic.isChecked() == False:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                intrl_disp_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        elif self.cb_dt_dynamic.isChecked() == True:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                time_series_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        response_multinode_dynamic.append(res_dynamic)
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Rotation, Rz", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "RFx":
                    response_multinode_dynamic = []
                    for i in range(len(nulti_node_dynamic)):
                        if ndm_v(main.fileName) == 3:
                            res_dynamic = main.outfreactFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (3 * nulti_node_dynamic[i] - 2),
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_dynamic = main.outfreactFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (2 * nulti_node_dynamic[i] - 1),
                            ]
                        if self.cb_dt_dynamic.isChecked() == False:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                intrl_disp_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        elif self.cb_dt_dynamic.isChecked() == True:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                time_series_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        response_multinode_dynamic.append(res_dynamic)
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Force Reaction, RFx", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "RFy":
                    response_multinode_dynamic = []
                    for i in range(len(nulti_node_dynamic)):
                        if ndm_v(main.fileName) == 3:
                            res_dynamic = main.outfreactFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (3 * nulti_node_dynamic[i] - 1),
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_dynamic = main.outfreactFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (2 * nulti_node_dynamic[i]),
                            ]
                        if self.cb_dt_dynamic.isChecked() == False:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                intrl_disp_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        elif self.cb_dt_dynamic.isChecked() == True:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                time_series_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        response_multinode_dynamic.append(res_dynamic)
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Force Reaction, Rz", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "RFz":
                    response_multinode_dynamic = []
                    for i in range(len(nulti_node_dynamic)):
                        if ndm_v(main.fileName) == 3:
                            res_dynamic = main.outfreactFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (3 * nulti_node_dynamic[i]),
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_dynamic = zero_2d_dynamic
                        if self.cb_dt_dynamic.isChecked() == False:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                intrl_disp_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        elif self.cb_dt_dynamic.isChecked() == True:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                time_series_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        response_multinode_dynamic.append(res_dynamic)
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Force Reaction, Rz", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "RMx":
                    response_multinode_dynamic = []
                    for i in range(len(nulti_node_dynamic)):
                        if ndm_v(main.fileName) == 3:
                            res_dynamic = main.outmreactFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (3 * nulti_node_dynamic[i] - 2),
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_dynamic = zero_2d_dynamic
                        if self.cb_dt_dynamic.isChecked() == False:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                intrl_disp_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        elif self.cb_dt_dynamic.isChecked() == True:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                time_series_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        response_multinode_dynamic.append(res_dynamic)
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Moment Reaction, RMx", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "RMy":
                    response_multinode_dynamic = []
                    for i in range(len(nulti_node_dynamic)):
                        if ndm_v(main.fileName) == 3:
                            res_dynamic = main.outmreactFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (3 * nulti_node_dynamic[i] - 1),
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_dynamic = zero_2d_dynamic
                        if self.cb_dt_dynamic.isChecked() == False:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                intrl_disp_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        elif self.cb_dt_dynamic.isChecked() == True:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                time_series_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        response_multinode_dynamic.append(res_dynamic)
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Moment Reaction, RMy", fontname="Times New Roman", size=10
                    )
                elif node_component_dynamic == "RMz":
                    response_multinode_dynamic = []
                    for i in range(len(nulti_node_dynamic)):
                        if ndm_v(main.fileName) == 3:
                            res_dynamic = main.outmreactFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (3 * nulti_node_dynamic[i]),
                            ]
                        elif ndm_v(main.fileName) == 2:
                            res_dynamic = main.outmreactFile[
                                main.step_statics : len(main.outdispFile[:, 1]),
                                (nulti_node_dynamic[i]),
                            ]
                        if self.cb_dt_dynamic.isChecked() == False:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                intrl_disp_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        elif self.cb_dt_dynamic.isChecked() == True:
                            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.plot(
                                time_series_dynamic,
                                res_dynamic,
                                linewidth=1,
                                label="Node " + str(nulti_node_dynamic[i]),
                            )
                        response_multinode_dynamic.append(res_dynamic)
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_ylabel(
                        "Moment Reaction, RMz", fontname="Times New Roman", size=10
                    )

                if self.cb_dt_dynamic.isChecked() == False:
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_xlabel(
                        "Interval", fontname="Times New Roman", size=10
                    )
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_xlim(
                        xmin=0, xmax=np.max(intrl_disp_dynamic)
                    )
                elif self.cb_dt_dynamic.isChecked() == True:
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_xlabel(
                        "Time (s)", fontname="Times New Roman", size=10
                    )
                    self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.set_xlim(
                        xmin=0, xmax=np.max(time_series_dynamic)
                    )
                legend = self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.legend(
                    fontsize=10, prop={"family": "Times New Roman"}
                )

            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.yaxis.offsetText.set_fontsize(
                9
            )
            self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.yaxis.offsetText.set_fontname(
                "Times New Roman"
            )

            for (
                tick
            ) in self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.get_xticklabels():
                tick.set_fontname("Times New Roman")
                tick.set_fontsize(9)
            for (
                tick
            ) in self.PdynamicWidget.canvas_pdynamic.axes_pdynamic.get_yticklabels():
                tick.set_fontname("Times New Roman")
                tick.set_fontsize(9)
            mpl.rcParams["savefig.dpi"] = 1000
            self.PdynamicWidget.canvas_pdynamic.draw()
        except:
            QMessageBox.critical(self, "Error", "Please check, unknown reason")

    def res_spectra(self):
        global index_cb, x_values, y_values, intrl_disp_dynamic
        try:
            index_cb = self.cb_resp_nodenumber_rs.currentIndex()
            intrl_disp_dynamic = np.linspace(
                0,
                (len(main.outdispFile[:, 1]) - main.step_statics - 1),
                (len(main.outdispFile[:, 1]) - main.step_statics),
            )

            zero_2d_dynamic = np.repeat(0, (len(intrl_disp_dynamic)))
            self.RespspectraWidget.canvas_rs.axes_rs.clear()

            try:
                self.RespspectraWidget.canvas_rs.axes_rs.set_facecolor(
                    str(plotresponse_dynamic_bg_color.name())
                )
            except:
                self.RespspectraWidget.canvas_rs.axes_rs.set_facecolor("#000000")
            try:
                self.RespspectraWidget.canvas_rs.axes_rs.grid(
                    True, which="both", color=str(plotresponse_dynamic_mg_color.name())
                )
            except:
                self.RespspectraWidget.canvas_rs.axes_rs.grid(
                    True, which="both", color="#ffffff"
                )
            try:
                self.RespspectraWidget.canvas_rs.axes_rs.grid(
                    True, which="both", linestyle=lstyle
                )
            except:
                self.RespspectraWidget.canvas_rs.axes_rs.grid(
                    True, which="both", linestyle="--"
                )
            try:
                self.RespspectraWidget.canvas_rs.axes_rs.grid(
                    True, which="both", linewidth=lwidth
                )
            except:
                self.RespspectraWidget.canvas_rs.axes_rs.grid(
                    True, which="both", linewidth=0.4
                )

            # if self.cb_multi_rs.isChecked()==False:
            if self.rbn_Ax.isChecked() == True:
                if ndm_v(main.fileName) == 3:
                    res_dynamic_rs = main.outaccFile[
                        main.step_statics : len(main.outdispFile[:, 1]),
                        (3 * index_cb + 1),
                    ]
                elif ndm_v(main.fileName) == 2:
                    res_dynamic_rs = main.outaccFile[
                        main.step_statics: len(main.outdispFile[:, 1]),
                        (2 * index_cb + 1),
                    ]
            elif self.rbn_Ay.isChecked() == True:
                if ndm_v(main.fileName) == 3:
                    res_dynamic_rs = main.outaccFile[
                        main.step_statics: len(main.outdispFile[:, 1]),
                        (3 * index_cb + 2),
                    ]
                elif ndm_v(main.fileName) == 2:
                    res_dynamic_rs = main.outaccFile[
                        main.step_statics: len(main.outdispFile[:, 1]),
                        (2 * index_cb + 2),
                    ]

            elif self.rbn_Az.isChecked() == True:
                if ndm_v(main.fileName) == 3:
                    res_dynamic_rs = main.outaccFile[
                        main.step_statics: len(main.outdispFile[:, 1]),
                        (3 * index_cb + 3),
                    ]
                elif ndm_v(main.fileName) == 2:
                    res_dynamic_rs = zero_2d_dynamic
            Tn, fz, Sd, SV, SA, PSa, PSv = resp_spectra(
                res_dynamic_rs,
                float(self.tb_dt_rs.text()),
                T_min=0.01,
                T_max=4,
                n_pts=200,
                Xi=float(self.tb_damping_rs.text()),
            )

            if self.rbn__T.isChecked() == True:
                x_values = Tn
                self.RespspectraWidget.canvas_rs.axes_rs.set_xlabel(
                    "Period (s)", fontname="Times New Roman", size=10
                )
            elif self.rbn_F.isChecked() == True:
                x_values = fz
                self.RespspectraWidget.canvas_rs.axes_rs.set_xlabel(
                    "Frequency (Hz)", fontname="Times New Roman", size=10
                )
            if self.rbn_PSa.isChecked() == True:
                y_values = PSa
                self.RespspectraWidget.canvas_rs.axes_rs.set_ylabel(
                    "Pseudo Spectral Acceleration, PSa",
                    fontname="Times New Roman",
                    size=10,
                )
            elif self.rbn_PSv.isChecked() == True:
                y_values = PSv
                self.RespspectraWidget.canvas_rs.axes_rs.set_ylabel(
                    "Pseudo Spectral Velocity, PSv", fontname="Times New Roman", size=10
                )
            elif self.rbn_Sd.isChecked() == True:
                y_values = Sd
                self.RespspectraWidget.canvas_rs.axes_rs.set_ylabel(
                    "Spectral Displacement, Sd", fontname="Times New Roman", size=10
                )

            elif self.rbn_Sa.isChecked() == True:
                y_values = SA
                self.RespspectraWidget.canvas_rs.axes_rs.set_ylabel(
                    "Spectral Acceleration, Sa", fontname="Times New Roman", size=10
                )
            elif self.rbn_Sv.isChecked() == True:
                y_values = SV
                self.RespspectraWidget.canvas_rs.axes_rs.set_ylabel(
                    "Spectral Velocity, Sv", fontname="Times New Roman", size=10
                )
            self.RespspectraWidget.canvas_rs.axes_rs.plot(
                x_values, y_values, color="r", linewidth=1
            )
            self.RespspectraWidget.canvas_rs.axes_rs.set_xlim(
                xmin=0, xmax=np.max(x_values)
            )
            for tick in self.RespspectraWidget.canvas_rs.axes_rs.get_xticklabels():
                tick.set_fontname("Times New Roman")
                tick.set_fontsize(9)
            for tick in self.RespspectraWidget.canvas_rs.axes_rs.get_yticklabels():
                tick.set_fontname("Times New Roman")
                tick.set_fontsize(9)
            mpl.rcParams["savefig.dpi"] = 1000
            self.RespspectraWidget.canvas_rs.draw()
        except:
            QMessageBox.critical(self, "Error", "Please check, unknown reason")


class about(QDialog, UI_about):
    def __init__(self, parent=None):
        super(about, self).__init__(parent)
        # uic.loadUi('UI/about.ui', self)
        self.setupUi(self)


class load_setting(QDialog, UI_LoadSetting):
    def __init__(self, parent=None):
        super(load_setting, self).__init__(parent)
        # uic.loadUi('UI/LoadSetting.ui', self)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.arrow_sizes)

    def arrow_sizes(self):
        global load_arrow_size, load_font_size, load_arrow_color, load_font_color
        load_arrow_size = float(self.tb_ls_arrow_size.text())
        load_font_size = int(self.tb_ls_font_size.text())
        load_arrow_color = self.cb_ls_arrow_color.currentText()
        load_font_color = self.cb_ls_font_color.currentText()


class load_setting_btn(QDialog, UI_LoadSetting):
    def __init__(self, parent=None):
        super(load_setting_btn, self).__init__(parent)
        # uic.loadUi('UI/LoadSetting.ui', self)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.arrow_sizes_btn)

    def arrow_sizes_btn(self):
        # global load_arrow_size, load_font_size, load_arrow_color, load_font_color
        load_arrow_size = float(self.tb_ls_arrow_size.text())
        load_font_size = int(self.tb_ls_font_size.text())
        load_arrow_color = self.cb_ls_arrow_color.currentText()
        load_font_color = self.cb_ls_font_color.currentText()
        # point_load(main.fileName, main.p, load_arrow_size, load_font_size, load_arrow_color, load_font_color)


class table_static(QDialog, UI_DataTable_Static):
    def __init__(self, parent=None):
        super(table_static, self).__init__(parent)
        # uic.loadUi('UI/DataTable_Static.ui', self)
        self.setupUi(self)
        self.btn_save_data_static.clicked.connect(self.save_data_static)
        nodes = node(main.fileName)[:, 1].astype(int)
        all_nodes = nodes.reshape((-1, 1))
        self.tableWidget_static.setColumnCount(16)
        self.tableWidget_static.setRowCount(len(all_nodes[:, 0]))
        node_cords = NodeCoords(main.fileName)
        if all_nodes.size > 0:
            for i in range(len(all_nodes[:, 0])):
                for j in range(1):
                    self.tableWidget_static.setItem(
                        i, j, QTableWidgetItem(str(all_nodes[i][j]))
                    )
        if node_cords.size > 0:
            for i in range(len(all_nodes[:, 0])):
                for j in range(3):
                    self.tableWidget_static.setItem(
                        i, j + 1, QTableWidgetItem(str(node_cords[i][j]))
                    )
        if main.recorder_disp == 1:
            def_static = main.deformation
            for i in range(len(all_nodes[:, 0])):
                for j in range(3):
                    self.tableWidget_static.setItem(
                        i, j + 4, QTableWidgetItem(str(np.round(def_static[i][j], 8)))
                    )
        if main.recorder_rot == 1:
            rot_static = main.rotation
            for i in range(len(all_nodes[:, 0])):
                for j in range(3):
                    self.tableWidget_static.setItem(
                        i, j + 7, QTableWidgetItem(str(np.round(rot_static[i][j], 8)))
                    )
        if main.recorder_force == 1:
            force_static = main.forcereaction
            for i in range(len(all_nodes[:, 0])):
                for j in range(3):
                    self.tableWidget_static.setItem(
                        i,
                        j + 10,
                        QTableWidgetItem(str(np.round(force_static[i][j], 8))),
                    )
        if main.recorder_moment == 1:
            moment_static = main.momentreaction
            for i in range(len(all_nodes[:, 0])):
                for j in range(3):
                    self.tableWidget_static.setItem(
                        i,
                        j + 13,
                        QTableWidgetItem(str(np.round(moment_static[i][j], 8))),
                    )

    def save_data_static(self):
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save Static Result File", "", ".xls(*.xls)"
        )
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("ResultSheet_Static", cell_overwrite_ok=True)
        sheet.col(0).width = 4000
        sheet.col(1).width = 4000
        sheet.col(2).width = 4000
        sheet.col(3).width = 4000
        sheet.col(4).width = 4000
        sheet.col(5).width = 4000
        sheet.col(6).width = 4000
        sheet.col(7).width = 4000
        sheet.col(8).width = 4000
        sheet.col(9).width = 4000
        sheet.col(10).width = 4000
        sheet.col(11).width = 4000
        sheet.col(12).width = 4000
        sheet.col(13).width = 4000
        sheet.col(14).width = 4000
        sheet.col(15).width = 4000

        style = xlwt.XFStyle()
        style1 = xlwt.XFStyle()
        style2 = xlwt.XFStyle()

        font = xlwt.Font()
        font.bold = True
        font.colour_index = 1
        font1 = xlwt.Font()
        font1.bold = True
        font2 = xlwt.Font()
        style.font = font
        style1.font = font1
        style2.font = font2

        borders = xlwt.Borders()
        borders.left = borders.THIN
        borders.right = borders.THIN
        borders.top = borders.THIN
        borders.bottom = borders.THIN
        borders.left_colour = 0
        borders.right_colour = 0
        borders.top_colour = 0
        borders.bottom_colour = 0
        style.borders = borders
        style2.borders = borders

        bg = xlwt.Pattern()
        bg.pattern = bg.SOLID_PATTERN  # NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
        bg.pattern_fore_colour = 3
        style.pattern = bg

        aligment = xlwt.Alignment()
        aligment.horz = aligment.HORZ_CENTER
        aligment.vert = aligment.VERT_CENTER
        style.alignment = aligment
        style1.alignment = aligment
        style2.alignment = aligment

        sheet.write_merge(0, 0, 0, 15, "ANALYSIS BY FeView (v. 1.0) ", style=style1)
        sheet.write_merge(2, 2, 0, 15, "STATIC ANALYSIS RESULT : ", style=style1)

        # style = xlwt.XFStyle()
        # font = xlwt.Font()
        # font.bold = True
        # style.font = font
        model = self.tableWidget_static.model()
        for c in range(model.columnCount()):
            text = model.headerData(c, QtCore.Qt.Horizontal)
            sheet.write(3, c, text, style=style)

        # for r in range(model.rowCount()):
        #    text = model.headerData(r, QtCore.Qt.Vertical)
        #    sheet.write(r + 1, 0, text, style=style)

        for c in range(model.columnCount()):
            for r in range(model.rowCount()):
                text = model.data(model.index(r, c))
                sheet.write(r + 4, c, text, style=style2)
        wbk.save(filename)


class table_modal(QDialog, UI_DataTable_Modal):
    def __init__(self, parent=None):
        super(table_modal, self).__init__(parent)
        # uic.loadUi('UI/DataTable_Modal.ui', self)
        self.setupUi(self)
        self.btn_save_data_modal.clicked.connect(self.save_data_modal)
        # nodes = node(main.fileName)[:, 1].astype(int)
        if numModes.size > 0:
            period_file = os.path.join(main.result_directory, "Periods.out")
            outperiodFile = np.round(OpenSeesOutputRead(period_file), 6)
            Frequency = np.round((1 / OpenSeesOutputRead(period_file)), 6)
            Frequency_rps = np.round(Frequency * 2 * np.pi, 6)
            modes = int(numModes)
            self.tableWidget_Modal.setColumnCount(4)
            self.tableWidget_Modal.setRowCount(modes)
            mode_number = np.arange(1, modes + 1, 1).reshape(modes, 1)
            for i in range(modes):
                for j in range(1):
                    self.tableWidget_Modal.setItem(
                        i, j, QTableWidgetItem(str(mode_number[i][j]))
                    )
            for i in range(modes):
                for j in range(1):
                    self.tableWidget_Modal.setItem(
                        i, j + 1, QTableWidgetItem(str(outperiodFile[i][j]))
                    )
            for i in range(modes):
                for j in range(1):
                    self.tableWidget_Modal.setItem(
                        i, j + 2, QTableWidgetItem(str(Frequency[i][j]))
                    )

            for i in range(modes):
                for j in range(1):
                    self.tableWidget_Modal.setItem(
                        i, j + 3, QTableWidgetItem(str(Frequency_rps[i][j]))
                    )

    def save_data_modal(self):
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save Eigen Value Analysis Result File", "", ".xls(*.xls)"
        )
        wbk = xlwt.Workbook(encoding="utf-8")
        sheet = wbk.add_sheet("EigenAnalysis", cell_overwrite_ok=True)
        sheet.col(0).width = 4000
        sheet.col(1).width = 5120
        sheet.col(2).width = 5120
        sheet.col(3).width = 5120
        style = xlwt.XFStyle()
        style1 = xlwt.XFStyle()
        style2 = xlwt.XFStyle()
        font = xlwt.Font()
        font.bold = True
        font.colour_index = 1
        font1 = xlwt.Font()
        font1.bold = True
        font2 = xlwt.Font()
        style.font = font
        style1.font = font1
        style2.font = font2
        borders = xlwt.Borders()
        borders.left = borders.THIN
        borders.right = borders.THIN
        borders.top = borders.THIN
        borders.bottom = borders.THIN
        borders.left_colour = 0
        borders.right_colour = 0
        borders.top_colour = 0
        borders.bottom_colour = 0
        style.borders = borders
        style2.borders = borders
        bg = xlwt.Pattern()
        bg.pattern = bg.SOLID_PATTERN  # NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
        bg.pattern_fore_colour = 3
        style.pattern = bg
        aligment = xlwt.Alignment()
        aligment.horz = aligment.HORZ_CENTER
        aligment.vert = aligment.VERT_CENTER
        style.alignment = aligment
        style1.alignment = aligment
        style2.alignment = aligment
        sheet.write_merge(0, 0, 0, 3, "ANALYSIS BY FeView (v. 1.0) ", style=style1)
        sheet.write_merge(2, 2, 0, 3, "EIGENVALUE ANALYSIS RESULT : ", style=style1)
        model = self.tableWidget_Modal.model()
        for c in range(model.columnCount()):
            text = model.headerData(c, QtCore.Qt.Horizontal)
            sheet.write(3, cp, text, style=style)
        for c in range(model.columnCount()):
            for r in range(model.rowCount()):
                text = model.data(model.index(r, c))
                sheet.write(r + 4, c, text, style=style2)
        wbk.save(filename)


class table_dynamic(QDialog, UI_DataTable_Dynamic):
    def __init__(self, parent=None):
        super(table_dynamic, self).__init__(parent)
        # uic.loadUi('UI/DataTable_Dynamic.ui', self)
        self.setupUi(self)
        nodes = node(main.fileName)[:, 1].astype(int)
        self.tableWidget_dynamic_disp.setColumnCount(len(nodes) * 3 + 1)
        self.tableWidget_dynamic_disp.setRowCount(0)
        item_int = QtWidgets.QTableWidgetItem("Interval")
        self.tableWidget_dynamic_disp.setHorizontalHeaderItem(0, item_int)
        # if main.outdispFile.size>0:
        disp_dynamic = np.round(
            main.outdispFile[
                main.step_statics : len(main.outdispFile[:, 0]),
                1 : len(main.outdispFile[0, :]),
            ],
            10,
        )

        self.tableWidget_dynamic_disp.setColumnCount(len(disp_dynamic[0, :]) + 1)
        self.tableWidget_dynamic_disp.setRowCount(len(disp_dynamic[:, 0]))

        for i in range(len(nodes)):
            item_x = QtWidgets.QTableWidgetItem("Node " + str(nodes[i]) + ", Ux")
            self.tableWidget_dynamic_disp.setHorizontalHeaderItem((3 * i + 1), item_x)
            item_y = QtWidgets.QTableWidgetItem("Node " + str(nodes[i]) + ", Uy")
            self.tableWidget_dynamic_disp.setHorizontalHeaderItem((3 * i + 2), item_y)
            item_z = QtWidgets.QTableWidgetItem("Node " + str(nodes[i]) + ", Uz")
            self.tableWidget_dynamic_disp.setHorizontalHeaderItem((3 * i + 3), item_z)
        for i in range(len(disp_dynamic[:, 0])):
            for j in range(len(disp_dynamic[0, :])):
                self.tableWidget_dynamic_disp.setItem(
                    i, j + 1, QTableWidgetItem(str(disp_dynamic[i][j]))
                )
        for i in range(len(disp_dynamic[:, 0])):
            for j in range(1):
                self.tableWidget_dynamic_disp.setItem(i, j, QTableWidgetItem(str(i)))


def CreateMainWindows():
    global main
    app = QtWidgets.QApplication(sys.argv)
    splashscreen = QSplashScreen(QPixmap("UI/icon/FeView_LogoL.png"))
    splashscreen.show()
    time.sleep(1)
    window = FeViewMain()
    splashscreen.finish(window)
    main = FeViewMain()
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    CreateMainWindows()
