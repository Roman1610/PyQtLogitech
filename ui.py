# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui',
# licensing of 'ui.ui' applies.
#
# Created: Wed May 22 21:50:39 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(551, 457)
        MainWindow.setMinimumSize(QtCore.QSize(480, 457))
        MainWindow.setMaximumSize(QtCore.QSize(630, 457))
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setContentsMargins(16, -1, 16, -1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 10, -1, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(100, 100))
        self.label_3.setMaximumSize(QtCore.QSize(100, 100))
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_10.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(300, 90))
        self.label_4.setMaximumSize(QtCore.QSize(300, 90))
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)
        self.label_4.setMargin(0)
        self.label_4.setIndent(-1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("SF UI Display")
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.solidModeRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.solidModeRadioButton.setChecked(True)
        self.solidModeRadioButton.setObjectName("solidModeRadioButton")
        self.verticalLayout_5.addWidget(self.solidModeRadioButton)
        self.cycleModeRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.cycleModeRadioButton.setObjectName("cycleModeRadioButton")
        self.verticalLayout_5.addWidget(self.cycleModeRadioButton)
        self.breatheModeRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.breatheModeRadioButton.setObjectName("breatheModeRadioButton")
        self.verticalLayout_5.addWidget(self.breatheModeRadioButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(16, -1, -1, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.introCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.introCheckBox.setObjectName("introCheckBox")
        self.horizontalLayout_5.addWidget(self.introCheckBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem1)
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.colorLabel = QtWidgets.QLabel(self.splitter_3)
        self.colorLabel.setObjectName("colorLabel")
        self.colorLineEdit = QtWidgets.QLineEdit(self.splitter_3)
        self.colorLineEdit.setMaximumSize(QtCore.QSize(100, 25))
        self.colorLineEdit.setObjectName("colorLineEdit")
        self.verticalLayout_9.addWidget(self.splitter_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.brightnessHorizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.brightnessHorizontalSlider.setMinimumSize(QtCore.QSize(250, 20))
        self.brightnessHorizontalSlider.setMaximumSize(QtCore.QSize(250, 20))
        self.brightnessHorizontalSlider.setMinimum(1)
        self.brightnessHorizontalSlider.setMaximum(100)
        self.brightnessHorizontalSlider.setSingleStep(10)
        self.brightnessHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.brightnessHorizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.brightnessHorizontalSlider.setTickInterval(10)
        self.brightnessHorizontalSlider.setObjectName("brightnessHorizontalSlider")
        self.horizontalLayout_2.addWidget(self.brightnessHorizontalSlider)
        self.brightnessLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.brightnessLineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.brightnessLineEdit.setMaximumSize(QtCore.QSize(70, 30))
        self.brightnessLineEdit.setStyleSheet("")
        self.brightnessLineEdit.setInputMask("")
        self.brightnessLineEdit.setMaxLength(32767)
        self.brightnessLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.brightnessLineEdit.setObjectName("brightnessLineEdit")
        self.horizontalLayout_2.addWidget(self.brightnessLineEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.rateLabel = QtWidgets.QLabel(self.centralwidget)
        self.rateLabel.setObjectName("rateLabel")
        self.verticalLayout_7.addWidget(self.rateLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cycleRateHorizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.cycleRateHorizontalSlider.setMinimumSize(QtCore.QSize(250, 20))
        self.cycleRateHorizontalSlider.setMaximumSize(QtCore.QSize(250, 20))
        self.cycleRateHorizontalSlider.setMinimum(100)
        self.cycleRateHorizontalSlider.setMaximum(60000)
        self.cycleRateHorizontalSlider.setSingleStep(2000)
        self.cycleRateHorizontalSlider.setProperty("value", 100)
        self.cycleRateHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.cycleRateHorizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.cycleRateHorizontalSlider.setTickInterval(2000)
        self.cycleRateHorizontalSlider.setObjectName("cycleRateHorizontalSlider")
        self.horizontalLayout_3.addWidget(self.cycleRateHorizontalSlider)
        self.rateLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.rateLineEdit.setMaximumSize(QtCore.QSize(70, 30))
        self.rateLineEdit.setObjectName("rateLineEdit")
        self.horizontalLayout_3.addWidget(self.rateLineEdit)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.horizontalLayout_7.addLayout(self.verticalLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        spacerItem4 = QtWidgets.QSpacerItem(20, 85, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.resetPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetPushButton.setObjectName("resetPushButton")
        self.horizontalLayout_8.addWidget(self.resetPushButton)
        self.applyPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyPushButton.setObjectName("applyPushButton")
        self.horizontalLayout_8.addWidget(self.applyPushButton)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><img src=\":/pngs/logo.png\"/></p></body></html>", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><img src=\":/pngs/Logitech_logo.png\"/></p></body></html>", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Mode", None, -1))
        self.solidModeRadioButton.setText(QtWidgets.QApplication.translate("MainWindow", "Solid", None, -1))
        self.cycleModeRadioButton.setText(QtWidgets.QApplication.translate("MainWindow", "Cycle", None, -1))
        self.breatheModeRadioButton.setText(QtWidgets.QApplication.translate("MainWindow", "Breathe", None, -1))
        self.introCheckBox.setText(QtWidgets.QApplication.translate("MainWindow", "Intro", None, -1))
        self.colorLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Enter a hex color:", None, -1))
        self.colorLineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "00FFFF", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Brightness:", None, -1))
        self.brightnessLineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.rateLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Cycle rate:", None, -1))
        self.rateLineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.resetPushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Reset", None, -1))
        self.applyPushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Apply", None, -1))