"""
mini-gps by ali
https://github.com/Ali-Almarri/leo_mini_GPS
"""

import csv
import struct
import time

import usb.core
import usb.util
from PyQt5 import QtCore, QtGui, QtTest, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow
from qwt import QwtPlot

from plaintextedit import PlainTextEdit


class Ui_MainWindow(QMainWindow):
    """to-do"""

    def __init__(self):
        """to-do"""
        super().__init__()

        self.setupUi()
        self.is_dev2_init = False
        self.stop_threads = False
        self.GPS_REFRENCE = 137216
        self.N31 = 1
        self.N2_HS = 11
        self.N2_LS = 3072
        self.N1_HS = 11
        self.NC1_LS = 1048576
        self.BW = 9
        self.dev = self.init_usb_hid()
        self.blinking = False
        self.one_time = False

    def setupUi(self):
        """to-do"""

        self.setObjectName("MainWindow")
        self.setFixedSize(380, 657)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 351, 171))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_device_name = QtWidgets.QLabel(self.groupBox)
        self.label_device_name.setGeometry(QtCore.QRect(120, 40, 191, 17))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_device_name.setFont(font)
        self.label_device_name.setObjectName("label_device_name")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_firmware = QtWidgets.QLabel(self.groupBox)
        self.label_firmware.setGeometry(QtCore.QRect(120, 100, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_firmware.setFont(font)
        self.label_firmware.setObjectName("label_firmware")
        self.label_made_by = QtWidgets.QLabel(self.groupBox)
        self.label_made_by.setGeometry(QtCore.QRect(120, 70, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_made_by.setFont(font)
        self.label_made_by.setObjectName("label_made_by")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 130, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_seria_number = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_seria_number.setEnabled(False)
        self.comboBox_seria_number.setGeometry(QtCore.QRect(120, 127, 151, 25))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.comboBox_seria_number.setFont(font)
        self.comboBox_seria_number.setObjectName("comboBox_seria_number")
        self.comboBox_seria_number.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 200, 351, 191))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.groupBox_2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(189, 43, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.btn_set_freq = QtWidgets.QPushButton(
            self.groupBox_2, clicked=lambda: self.btn_set_freq_clicked()
        )
        self.btn_set_freq.setGeometry(QtCore.QRect(30, 80, 141, 25))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.btn_set_freq.setFont(font)
        self.btn_set_freq.setObjectName("btn_set_freq")
        self.btn_factory_defaults = QtWidgets.QPushButton(
            self.groupBox_2, clicked=lambda: self.btn_factory_defaults_clicked()
        )
        self.btn_factory_defaults.setGeometry(QtCore.QRect(30, 120, 141, 25))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.btn_factory_defaults.setFont(font)
        self.btn_factory_defaults.setObjectName("btn_factory_defaults")
        self.btn_advanced = QtWidgets.QPushButton(
            self.groupBox_2, clicked=lambda: self.btn_advanced_clicked()
        )
        self.btn_advanced.setGeometry(QtCore.QRect(190, 120, 141, 25))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.btn_advanced.setFont(font)
        self.btn_advanced.setObjectName("btn_advanced")
        self.textEdit_output_freq = PlainTextEdit(self.groupBox_2)
        self.textEdit_output_freq.setGeometry(QtCore.QRect(30, 40, 140, 26))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.textEdit_output_freq.setFont(font)
        self.textEdit_output_freq.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.textEdit_output_freq.setLineWidth(1)
        self.textEdit_output_freq.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.textEdit_output_freq.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.textEdit_output_freq.setLineWrapMode(PlainTextEdit.NoWrap)
        self.textEdit_output_freq.setObjectName("textEdit_output_freq")
        rx = QtCore.QRegExp(
            "(36[5-9]|3[7-9]\d|[4-9]\d{2,10}|[1-9]\d{3,7}|[1-7]\d{8}|80\d{7}|81[01]\d{6}|812[0-5]\d{7}|812500000)"
        )  # +++
        QtGui.QRegExpValidator(rx)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(400, 20, 401, 591))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(140, 46, 161, 17))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.comboBox_output_level = QtWidgets.QComboBox(self.groupBox_3)

        self.comboBox_output_level.setGeometry(QtCore.QRect(30, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.comboBox_output_level.setFont(font)
        self.comboBox_output_level.setObjectName("comboBox_output_level")
        self.comboBox_output_level.addItem("")
        self.comboBox_output_level.addItem("")
        self.comboBox_output_level.addItem("")
        self.comboBox_output_level.addItem("")
        self.checkBox_enable_output = QtWidgets.QCheckBox(
            self.groupBox_3, clicked=lambda: self.set_output()
        )
        self.checkBox_enable_output.setGeometry(QtCore.QRect(35, 100, 121, 23))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.checkBox_enable_output.setFont(font)
        self.checkBox_enable_output.setObjectName("checkBox")
        self.line = QtWidgets.QFrame(self.groupBox_3)
        self.line.setGeometry(QtCore.QRect(10, 160, 371, 20))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btn_blink_led = QtWidgets.QPushButton(
            self.groupBox_3, clicked=lambda: self.btn_blink_led_clicked()
        )
        self.btn_blink_led.setGeometry(QtCore.QRect(240, 100, 141, 25))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.btn_blink_led.setFont(font)
        self.btn_blink_led.setObjectName("btn_blink_led")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(158, 183, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(158, 224, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.textEdit_n31 = PlainTextEdit(self.groupBox_3)
        self.textEdit_n31.setGeometry(QtCore.QRect(40, 220, 105, 26))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.textEdit_n31.setFont(font)
        self.textEdit_n31.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_n31.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_n31.setLineWrapMode(PlainTextEdit.NoWrap)
        self.textEdit_n31.setObjectName("textEdit_n31")
        self.textEdit_n2_hs = PlainTextEdit(self.groupBox_3)
        self.textEdit_n2_hs.setGeometry(QtCore.QRect(40, 260, 105, 26))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.textEdit_n2_hs.setFont(font)
        self.textEdit_n2_hs.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_n2_hs.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_n2_hs.setLineWrapMode(PlainTextEdit.NoWrap)
        self.textEdit_n2_hs.setObjectName("textEdit_n2_hs")
        self.textEdit_n1_hs = PlainTextEdit(self.groupBox_3)
        self.textEdit_n1_hs.setGeometry(QtCore.QRect(40, 340, 105, 26))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.textEdit_n1_hs.setFont(font)
        self.textEdit_n1_hs.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_n1_hs.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_n1_hs.setLineWrapMode(PlainTextEdit.NoWrap)
        self.textEdit_n1_hs.setObjectName("textEdit_n1_hs")
        self.textEdit_n2_ls = PlainTextEdit(self.groupBox_3)
        self.textEdit_n2_ls.setGeometry(QtCore.QRect(40, 300, 105, 26))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.textEdit_n2_ls.setFont(font)
        self.textEdit_n2_ls.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_n2_ls.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_n2_ls.setLineWrapMode(PlainTextEdit.NoWrap)
        self.textEdit_n2_ls.setObjectName("textEdit_n2_ls")
        self.textEdit_nc1_ls = PlainTextEdit(self.groupBox_3)
        self.textEdit_nc1_ls.setGeometry(QtCore.QRect(40, 380, 105, 26))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.textEdit_nc1_ls.setFont(font)
        self.textEdit_nc1_ls.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_nc1_ls.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_nc1_ls.setLineWrapMode(PlainTextEdit.NoWrap)
        self.textEdit_nc1_ls.setObjectName("textEdit_nc1_ls")
        self.textEdit_bw = PlainTextEdit(self.groupBox_3)
        self.textEdit_bw.setGeometry(QtCore.QRect(40, 420, 105, 26))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.textEdit_bw.setFont(font)
        self.textEdit_bw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_bw.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_bw.setLineWrapMode(PlainTextEdit.NoWrap)
        self.textEdit_bw.setObjectName("textEdit_bw")
        self.textEdit_gps_reference = PlainTextEdit(self.groupBox_3)
        self.textEdit_gps_reference.setGeometry(QtCore.QRect(40, 180, 105, 26))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.textEdit_gps_reference.setFont(font)
        self.textEdit_gps_reference.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.textEdit_gps_reference.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff
        )
        self.textEdit_gps_reference.setLineWrapMode(PlainTextEdit.NoWrap)
        self.textEdit_gps_reference.setObjectName("textEdit_gps_reference")
        self.label_n2_ls = QtWidgets.QLabel(self.groupBox_3)
        self.label_n2_ls.setGeometry(QtCore.QRect(158, 303, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.label_n2_ls.setFont(font)
        self.label_n2_ls.setObjectName("label_n2_ls")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(158, 264, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_nc1_ls = QtWidgets.QLabel(self.groupBox_3)
        self.label_nc1_ls.setGeometry(QtCore.QRect(158, 384, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.label_nc1_ls.setFont(font)
        self.label_nc1_ls.setObjectName("label_nc1_ls")
        self.label_n1_hs = QtWidgets.QLabel(self.groupBox_3)
        self.label_n1_hs.setGeometry(QtCore.QRect(158, 345, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.label_n1_hs.setFont(font)
        self.label_n1_hs.setObjectName("label_n1_hs")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(160, 427, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.line_2 = QtWidgets.QFrame(self.groupBox_3)
        self.line_2.setGeometry(QtCore.QRect(20, 470, 371, 20))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.btn_update = QtWidgets.QPushButton(
            self.groupBox_3, clicked=lambda: self.btn_update_clicked()
        )
        self.btn_update.setGeometry(QtCore.QRect(244, 424, 141, 25))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.btn_update.setFont(font)
        self.btn_update.setObjectName("btn_update")
        self.label_position = QtWidgets.QLabel(self.groupBox_3)
        self.label_position.setGeometry(QtCore.QRect(30, 510, 341, 20))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.label_position.setFont(font)
        self.label_position.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_position.setObjectName("label_position")
        self.label_utc = QtWidgets.QLabel(self.groupBox_3)
        self.label_utc.setGeometry(QtCore.QRect(30, 540, 341, 20))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.label_utc.setFont(font)
        self.label_utc.setObjectName("label_utc")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 400, 351, 211))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_gps_signal = QtWidgets.QLabel(self.groupBox_4)
        self.label_gps_signal.setGeometry(QtCore.QRect(20, 170, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.label_gps_signal.setFont(font)
        self.label_gps_signal.setStyleSheet(
            "background-color: rgb(115, 210, 22);\n" "border: 1px solid black;"
        )
        self.label_gps_signal.setObjectName("label_gps_signal")
        self.label_pll_signal = QtWidgets.QLabel(self.groupBox_4)
        self.label_pll_signal.setGeometry(QtCore.QRect(180, 170, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(11)
        self.label_pll_signal.setFont(font)
        self.label_pll_signal.setStyleSheet(
            "background-color: rgb(115, 210, 22);\n" "border: 1px solid black;"
        )
        self.label_pll_signal.setObjectName("label_pll_signal")
        self.qwtPlot = QwtPlot(self.groupBox_4)
        self.qwtPlot.setGeometry(QtCore.QRect(0, 40, 311, 131))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        self.qwtPlot.setFont(font)
        self.qwtPlot.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.qwtPlot.setAutoFillBackground(False)
        self.qwtPlot.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.qwtPlot.setFrameShadow(QtWidgets.QFrame.Plain)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.qwtPlot.setCanvasBackground(brush)
        self.qwtPlot.setAutoReplot(False)
        self.qwtPlot.setObjectName("qwtPlot")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.comboBox_output_level.currentIndexChanged.connect(self.change_power)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.timer = QTimer()
        self.timer.singleShot(0, self.loop)
        self.timer.start(200)

        self.show()

    def retranslateUi(self):
        """to-do"""
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", ""))
        self.groupBox.setTitle(_translate("MainWindow", "Hardware details"))
        self.label_device_name.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", "Firmware version"))
        self.label_firmware.setText(_translate("MainWindow", ""))
        self.label_made_by.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", "Made by"))
        self.label_7.setText(_translate("MainWindow", "Serial number"))
        self.label.setText(_translate("MainWindow", "Device name"))
        self.comboBox_seria_number.setItemText(0, _translate("MainWindow", ""))
        self.groupBox_2.setTitle(_translate("MainWindow", "Settings"))
        self.label_8.setText(_translate("MainWindow", "Output, Hz"))
        self.btn_set_freq.setText(_translate("MainWindow", "Set frequency"))
        self.btn_factory_defaults.setText(_translate("MainWindow", "Factory defaults"))
        self.btn_advanced.setText(_translate("MainWindow", "Advanced >>>"))
        self.textEdit_output_freq.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Liberation Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Ubuntu\';">10000000</span></p></body></html>',
            )
        )
        self.groupBox_3.setTitle(_translate("MainWindow", "Advanced"))
        self.label_9.setText(_translate("MainWindow", "Output drive strength"))
        self.comboBox_output_level.setItemText(0, _translate("MainWindow", "8mA"))
        self.comboBox_output_level.setItemText(1, _translate("MainWindow", "16mA"))
        self.comboBox_output_level.setItemText(2, _translate("MainWindow", "24mA"))
        self.comboBox_output_level.setItemText(3, _translate("MainWindow", "32mA"))

        self.checkBox_enable_output.setText(_translate("MainWindow", "Enable output"))
        self.checkBox_enable_output.setChecked(True)
        self.btn_blink_led.setText(_translate("MainWindow", "Blink LED"))
        self.label_10.setText(_translate("MainWindow", "GPS reference, Hz"))
        self.label_11.setText(_translate("MainWindow", "N31"))
        self.textEdit_n31.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Liberation Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Ubuntu\';">1500</span></p></body></html>',
            )
        )
        self.textEdit_n2_hs.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Liberation Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Ubuntu\';">1500</span></p></body></html>',
            )
        )
        self.textEdit_n1_hs.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Liberation Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Ubuntu\';">1500</span></p></body></html>',
            )
        )
        self.textEdit_n2_ls.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Liberation Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Ubuntu\';">1500</span></p></body></html>',
            )
        )
        self.textEdit_nc1_ls.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Liberation Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Ubuntu\';">1500</span></p></body></html>',
            )
        )
        self.textEdit_bw.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Liberation Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Ubuntu\';">1500</span></p></body></html>',
            )
        )
        self.textEdit_gps_reference.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Liberation Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:\'Ubuntu\';">1500</span></p></body></html>',
            )
        )
        self.label_n2_ls.setText(_translate("MainWindow", "N2_LS"))
        self.label_13.setText(_translate("MainWindow", "N2_HS"))
        self.label_nc1_ls.setText(_translate("MainWindow", "NC1_LS"))
        self.label_n1_hs.setText(_translate("MainWindow", "N1_HS"))
        self.label_16.setText(_translate("MainWindow", "BW"))
        self.btn_update.setText(_translate("MainWindow", "Update"))
        self.label_position.setText(_translate("MainWindow", "Position:"))
        self.label_utc.setText(_translate("MainWindow", "UTC:"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Status"))

        self.label_gps_signal.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center">GPS signal OK</p></body></html>',
            )
        )
        self.label_pll_signal.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center">PLL lock OK</p></body></html>',
            )
        )

    def change_power(self, value):
        """to-do"""
        self.hid_set_report(bytearray.fromhex("03 0" + str(value) + " 00 00"))

    def set_output(self):
        """to-do"""

        value = self.checkBox_enable_output.isChecked()
        if value:
            self.hid_set_report(bytearray.fromhex("01 03 00 00"))
        else:
            self.hid_set_report(bytearray.fromhex("01 00 00 00"))

    def btn_advanced_clicked(self):
        """to-do"""
        width = self.frameGeometry().width()
        if width > 480:
            self.setFixedSize(380, 657)
            self.btn_advanced.setText("Advanced >>>")

        if width < 480:
            self.setFixedSize(820, 657)
            self.btn_advanced.setText("Advanced <<<")

    def btn_factory_defaults_clicked(self):
        """to-do"""
        try:
            loc_out_freq = str(10000000)

            setFreqDict = self.convert_csv_toDict()
            dict_index = setFreqDict["output_freq"].index(loc_out_freq)

            loc_GPSFrequency = setFreqDict["GPS_reference"][dict_index]
            loc_n31 = setFreqDict["N31"][dict_index]
            loc_N2_HS = setFreqDict["N2_HS"][dict_index]
            loc_N2_LS = setFreqDict["N2_LS"][dict_index]
            loc_N1_HS = setFreqDict["N1_HS"][dict_index]
            loc_NC1_LS = setFreqDict["NC1_LS"][dict_index]
            loc_BW = setFreqDict["BW"][dict_index]
            self.textEdit_gps_reference.setText(str(loc_GPSFrequency))
            self.textEdit_n31.setText(str(loc_n31))
            self.textEdit_n2_hs.setText(str(loc_N2_HS))
            self.textEdit_n2_ls.setText(str(loc_N2_LS))
            self.textEdit_n1_hs.setText(str(loc_N1_HS))
            self.textEdit_nc1_ls.setText(str(loc_NC1_LS))
            self.textEdit_bw.setText(str(loc_BW))
            self.textEdit_output_freq.setText(loc_out_freq)
            self.textEdit_output_freq.setAlignment(QtCore.Qt.AlignHCenter)
            self.setting_to_buffer()
        except ValueError:
            print(loc_out_freq, "not in list")

    def btn_set_freq_clicked(self):
        """to-do"""

        #                 # loc_VCO = ((loc_GPSFrequency) / (loc_n31)) * (loc_N2_HS) * (loc_N2_LS);
        #                 # loc_Frequency1 = loc_VCO / (loc_N1_HS) / (loc_NC1_LS);
        #         # loc_GPSFreq    f3       +-------+                                     fout1
        #         # ------> ÷ loc_N3 -----> |       |   fosc                 +-> ÷ NC1_LS -------->
        #         #                         |  PLL  | ------+--> ÷ N1_HS --|
        #         #         +------->       |       |         |              +-> ÷ NC2_LS -------->
        #         #         |               +-------+         |                           fout2
        #         #         |                                 |
        #         #         +-- ÷ loc_N2_LS <--- ÷ loc_N2_HS <--+

        #         # fin   =                                   10.000 kHz ...  16.000 MHz
        #         # f3    = fin / loc_n31                  =  10.000 kHz ...   2.000 MHz
        #         # fosc  = fin * (N2_LS * N2_HS) / N3     =   4.850 GHz ...   5.670 GHz
        #         # fout1 = fosc / (N1_HS * NC1_LS)        = 450.000 Hz  ... 808.000 MHz
        #         # fout2 = fosc / (N1_HS * NC2_LS)        = 450.000 Hz  ... 808.000 MHz

        try:
            loc_out_freq = self.textEdit_output_freq.toPlainText()
            setFreqDict = self.convert_csv_toDict()
            dict_index = setFreqDict["output_freq"].index(loc_out_freq)

            loc_GPSFrequency = setFreqDict["GPS_reference"][dict_index]
            loc_n31 = setFreqDict["N31"][dict_index]
            loc_N2_HS = setFreqDict["N2_HS"][dict_index]
            loc_N2_LS = setFreqDict["N2_LS"][dict_index]
            loc_N1_HS = setFreqDict["N1_HS"][dict_index]
            loc_NC1_LS = setFreqDict["NC1_LS"][dict_index]
            loc_BW = setFreqDict["BW"][dict_index]
            self.textEdit_gps_reference.setText(str(loc_GPSFrequency))
            self.textEdit_n31.setText(str(loc_n31))
            self.textEdit_n2_hs.setText(str(loc_N2_HS))
            self.textEdit_n2_ls.setText(str(loc_N2_LS))
            self.textEdit_n1_hs.setText(str(loc_N1_HS))
            self.textEdit_nc1_ls.setText(str(loc_NC1_LS))
            self.textEdit_bw.setText(str(loc_BW))
            self.setting_to_buffer()
        except ValueError:
            print(loc_out_freq, "not in list")

    def btn_blink_led_clicked(self):
        """to-do"""

        if self.blinking:
            self.hid_set_report(bytearray.fromhex("02 00 00"))
            self.blinking = False
        else:
            self.hid_set_report(bytearray.fromhex("02 01 00"))
            self.blinking = True

    def btn_update_clicked(self):
        """to-do"""
        self.setting_to_buffer()
        self.get_setting()
        print("update done")

    def convert_csv_toDict(self):
        """to-do"""

        with open(
            "mini_gps_data - Data by one.csv", encoding="utf-8", mode="r"
        ) as file:
            reader = csv.DictReader(file)
            output_freq = {
                "output_freq": [],
                "GPS_reference": [],
                "N31": [],
                "N2_HS": [],
                "N2_LS": [],
                "N1_HS": [],
                "NC1_LS": [],
                "BW": [],
            }
            for record in reader:
                # print(record)
                output_freq["output_freq"].append(record["output_freq"])
                output_freq["GPS_reference"].append(record["GPS_reference"])
                output_freq["N31"].append(record["N31"])
                output_freq["N2_HS"].append(record["N2_HS"])
                output_freq["N2_LS"].append(record["N2_LS"])
                output_freq["N1_HS"].append(record["N1_HS"])
                output_freq["NC1_LS"].append(record["NC1_LS"])
                output_freq["BW"].append(record["BW"])

        return output_freq

    def hid_set_report(self, report):
        """Implements HID SetReport via USB control transfer"""
        try:
            self.dev.ctrl_transfer(
                0x21,  # REQUEST_TYPE_CLASS | RECIPIENT_INTERFACE | ENDPOINT_OUT
                9,  # SET_REPORT
                0x300,  # "Vendor" Descriptor Type + 0 Descriptor Index
                0,  # USB interface № 0
                report,  # the HID payload as a byte array -- e.g. from struct.pack()
            )
        except Exception:
            pass

    def hid_get_report(self):
        """Implements HID GetReport via USB control transfer"""

        try:

            return self.dev.ctrl_transfer(
                0xA1,  # REQUEST_TYPE_CLASS | RECIPIENT_INTERFACE | ENDPOINT_IN
                1,  # GET_REPORT
                0x309,  # "Vendor" Descriptor Type + 0 Descriptor Index
                0,  # USB interface № 0
                60,  # max reply size
            )
        except Exception:
            pass

    def read_interrupt(self):
        """
        *** read_interrupt to read gps signal status and pll status signal
        *** if res [1]  byte  is equal to some number change color label_pll_signal or label_gps_signal

        """

        try:
            buf = self.dev.read(0x81, 64, 100).tolist()
            print(buf[0])

            sat_lock = not bool(buf[1] & 0x01)
            pll_lock = not bool(buf[1] & 0x02)
            print(f"sat {sat_lock}\n pll {pll_lock}")
            if pll_lock == False and sat_lock == True:
                # no pll
                # gps ok
                self.label_pll_signal.setStyleSheet(
                    "background-color: rgb(207, 2, 2);\n" "border: 1px solid black;"
                )
                self.label_gps_signal.setStyleSheet(
                    "background-color: rgb(115, 210, 22);\n" "border: 1px solid black;"
                )
            elif pll_lock == True and sat_lock == False:
                # no gps
                # pll ok
                self.label_pll_signal.setStyleSheet(
                    "background-color: rgb(115, 210, 22);\n" "border: 1px solid black;"
                )
                self.label_gps_signal.setStyleSheet(
                    "background-color: rgb(207, 2, 2);\n" "border: 1px solid black;"
                )
            elif pll_lock == False and sat_lock == False:
                # no gps
                # no pll
                self.label_gps_signal.setStyleSheet(
                    "background-color: rgb(207, 2, 2);\n" "border: 1px solid black;"
                )
                self.label_gps_signal.setStyleSheet(
                    "background-color: rgb(207, 2, 2);\n" "border: 1px solid black;"
                )
            elif pll_lock == True and sat_lock == True:
                # gps ok
                #  pll ok
                self.label_pll_signal.setStyleSheet(
                    "background-color: rgb(115, 210, 22);\n" "border: 1px solid black;"
                )
                self.label_gps_signal.setStyleSheet(
                    "background-color: rgb(115, 210, 22);\n" "border: 1px solid black;"
                )

        except Exception:
            pass

    def init_usb_hid(self):
        """
        *** init_usb_hid to read gps signal status and pll status signal
        ***

        """
        self.dev = usb.core.find(idVendor=0x1DD2, idProduct=0x2211)

        if self.dev is None:
            return self.dev
        # interface = self.dev[0].interfaces()[0]
        self.endpoint = self.dev[0].interfaces()[0].endpoints()[0]

        i = self.dev[0].interfaces()[0].bInterfaceNumber
        time.sleep(0.5)
        if self.dev.is_kernel_driver_active(i):

            try:
                self.dev.detach_kernel_driver(i)
            except usb.core.USBError as e:
                sys.exit(
                    f"Could not detatch kernel driver from interface({i}): {str(e)}"
                )
        if self.dev is None:
            raise ValueError("Device not found")
        return self.dev

    def is_device_none(self):
        """to-do"""
        if self.dev is None:
            return False
        else:
            return True

    def clear_data(self):
        """to-do"""
        self.label_made_by.setText("")
        self.label_device_name.setText("")
        self.label_firmware.setText("")
        self.textEdit_output_freq.setText("")
        self.textEdit_gps_reference.setText(str(""))
        self.textEdit_n31.setText(str(""))
        self.textEdit_n2_hs.setText(str(""))
        self.textEdit_n2_ls.setText(str(""))
        self.textEdit_n1_hs.setText(str(""))
        self.textEdit_nc1_ls.setText(str(""))
        self.textEdit_bw.setText(str(""))
        self.comboBox_seria_number.setItemText(0, "")

    def fill_setting(self):
        """to-do"""
        self.textEdit_gps_reference.setText(str(self.GPS_REFRENCE))
        self.textEdit_n31.setText(str(self.N31))
        self.textEdit_n2_hs.setText(str(self.N2_HS))
        self.textEdit_n2_ls.setText(str(self.N2_LS))
        self.textEdit_n1_hs.setText(str(self.N1_HS))
        self.textEdit_nc1_ls.setText(str(self.NC1_LS))
        self.textEdit_bw.setText(str(self.BW))

    def fill_data(self):
        """to-do"""
        dev2 = usb.core.find(idVendor=0x1DD2, idProduct=0x2211)
        self.dev = dev2
        try:
            # Dev iManufacturer
            if self.dev._manufacturer is None:
                self.dev._manufacturer = usb.util.get_string(
                    self.dev, self.dev.iManufacturer
                )
                self.label_made_by.setText(self.dev._manufacturer)
            # Dev iProduct
            if self.dev._product is None:
                self.dev._product = usb.util.get_string(self.dev, self.dev.iProduct)
                self.label_device_name.setText(self.dev._product)
            # Dev iSerialNumber
            if self.dev._serial_number is None:
                self.dev._serial_number = usb.util.get_string(
                    self.dev, self.dev.iSerialNumber
                )
                self.comboBox_seria_number.setItemText(0, self.dev._serial_number)

                # Dev firmware_version
                firmware_hex = hex(self.dev.bcdDevice)[2:]
                major = str(firmware_hex[0])
                minor = str(firmware_hex[1:])
                firmware_version = str(major + "." + minor)
                self.label_firmware.setText(firmware_version)
        except Exception:
            pass

    def setting_to_buffer(self):
        """
        GPSFrequency size 3 bytes     START_LOCATION  2  add 1
        N31          size 3 bytes  START_LOCATION  5  add 1
        N2_HS        size 1 byte   START_LOCATION  8  add 4
        N2_LS        size 3 bytes  START_LOCATION  9  add 1
        N1_HS        size 1 byte   START_LOCATION  12 add 4
        NC1_LS       size 3 bytes  START_LOCATION  13 add 1
        NC2_LS       size 3 bytes  START_LOCATION  16 add 1
        BW           size 1 byte   START_LOCATION  20

        double VCO = (double(GPSFrequency) / double(N31)) * double(N2_HS) * double(N2_LS);
        double Frequency1 = VCO / double(N1_HS) / double(NC1_LS);
        double Frequency2 = VCO / double(N1_HS) / double(NC2_LS);
        TODO
        """

        loc_GPSFrequency = int(self.textEdit_gps_reference.toPlainText())
        loc_n31 = int(self.textEdit_n31.toPlainText())
        loc_N2_HS = int(self.textEdit_n2_hs.toPlainText())
        loc_N2_LS = int(self.textEdit_n2_ls.toPlainText())
        loc_N1_HS = int(self.textEdit_n1_hs.toPlainText())
        loc_NC1_LS = int(self.textEdit_nc1_ls.toPlainText())
        loc_NC2_LS = int(self.textEdit_nc1_ls.toPlainText())
        skew = 0
        loc_BW = int(self.textEdit_bw.toPlainText())

        # loc_VCO = ((loc_GPSFrequency) / (loc_n31)) * (loc_N2_HS) * (loc_N2_LS)
        # loc_Frequency1 = loc_VCO / (loc_N1_HS) / (loc_NC1_LS)

        buf = 60 * [0]
        buf[0] = 4
        buf[1:4] = struct.pack("<I", loc_GPSFrequency)[0:3]
        buf[4:7] = struct.pack("<I", loc_n31 - 1)[0:3]
        buf[7:8] = struct.pack("<B", loc_N2_HS - 4)[0:1]
        buf[8:11] = struct.pack("<I", loc_N2_LS - 1)[0:3]
        buf[11:12] = struct.pack("<B", loc_N1_HS - 4)[0:1]
        buf[12:15] = struct.pack("<I", loc_NC1_LS - 1)[0:3]
        buf[15:18] = struct.pack("<I", loc_NC2_LS - 1)[0:3]
        buf[18:19] = struct.pack("<B", skew)[0:1]
        buf[19:20] = struct.pack("<B", loc_BW)[0:1]
        # strPacket = str(buf)
        ba = bytearray(buf)

        # s = "".join(format(x, "02x") for x in ba)
        self.hid_set_report(ba)
        # self.textEdit_output_freq.setText(str(int(loc_Frequency1)))
        print("ok")

    def get_setting(self):
        """to-do"""
        try:
            buflist = self.hid_get_report().tolist()
            buf = bytearray(buflist)
            self.checkBox_enable_output.setChecked(bool(buf[0] & 0x01))
            loc_level = struct.unpack("<B", buf[1:2])[0]
            loc_GPSFrequency = struct.unpack("<I", buf[2:5] + bytes([0]))[0]
            loc_n31 = struct.unpack("<I", buf[5:8] + bytes([0]))[0] + 1
            loc_N2_HS = struct.unpack("<B", buf[8:9])[0] + 4
            loc_N2_LS = struct.unpack("<I", buf[9:12] + bytes([0]))[0] + 1
            loc_N1_HS = struct.unpack("<B", buf[12:13])[0] + 4
            loc_NC1_LS = struct.unpack("<I", buf[13:16] + bytes([0]))[0] + 1
            # loc_NC2_LS = struct.unpack("<I", buf[16:19] + bytes([0]))[0] + 1
            loc_BW = struct.unpack("<B", buf[20:21])[0]
            loc_VCO = ((loc_GPSFrequency) / (loc_n31)) * (loc_N2_HS) * (loc_N2_LS)
            loc_Frequency1 = loc_VCO / (loc_N1_HS) / (loc_NC1_LS)

            self.comboBox_output_level.setCurrentIndex(loc_level)
            self.textEdit_gps_reference.setText(str(loc_GPSFrequency))
            self.textEdit_n31.setText(str(loc_n31))
            self.textEdit_n2_hs.setText(str(loc_N2_HS))
            self.textEdit_n2_ls.setText(str(loc_N2_LS))
            self.textEdit_n1_hs.setText(str(loc_N1_HS))
            self.textEdit_nc1_ls.setText(str(loc_NC1_LS))

            self.textEdit_bw.setText(str(loc_BW))

            string = str(int(loc_Frequency1))
            self.textEdit_output_freq.setText(string)
            self.textEdit_output_freq.setAlignment(QtCore.Qt.AlignHCenter)
        except Exception:
            pass

    """
    load device information into the GUI
    """

    def divece_info(self):
        """to-do"""
        print("divece_info")
        self.dev = self.init_usb_hid()
        self.fill_data()
        self.get_setting()

    def loop(self):
        """to-do"""
        """
         *** loop()
         *** listen to usb if available or not
         *** load device information into the GUI

        """
        # import sys

        # print(time.time())
        dev2 = usb.core.find(idVendor=0x1DD2, idProduct=0x2211)
        # if self.stop_threads == True:
        #    return
        if dev2 is not None:

            if self.is_dev2_init == False:
                self.divece_info()
                print("dev found")
                self.is_dev2_init = True
                self.one_time = False

        else:
            self.clear_data()
            self.one_time = False
            self.is_dev2_init = False
            self.dev = None

        self.read_interrupt()
        if self.isHidden() is True:
            sys.exit()
        self.timer.stop()
        QtTest.QTest.qWait(1000)
        self.timer.start(1000)
        self.timer.singleShot(0, self.loop)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi()
    ui.convert_csv_toDict()

    sys.exit(app.exec_())
