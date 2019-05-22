import os
import sys
import traceback
from enum import Enum

from PySide2 import QtWidgets
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QLineEdit, QSlider

import g203led as logitech
from ui import Ui_MainWindow


class Mode(Enum):
    SOLID = 'solid'
    CYCLE = 'cycle'
    BREATHE = 'breathe'


mode = Mode(Mode.SOLID)
color = str()


# Create application
app = QtWidgets.QApplication(sys.argv)

# Create For and init ui
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

status_label = QtWidgets.QLabel(ui.statusBar)
ui.statusBar.addWidget(status_label)
timer = QTimer()


# Logic
def clear_status():
    status_label.clear()
    timer.stop()


def set_status(text: str, is_always=False):
    if timer.isActive():
        timer.stop()

    status_label.setText(text)
    if not is_always:
        timer.start(2000)


def is_user_admin():

    if os.name == 'nt':
        import ctypes
        # WARNING: requires Windows XP SP2 or higher!
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            traceback.print_exc()
            print("Admin check failed, assuming not an admin.")
            return False
    elif os.name == 'posix':
        # Check for root on Posix
        return os.getuid() == 0
    else:
        raise RuntimeError("Unsupported operating system for this module: %s" % os.name)


if is_user_admin() is False:
    set_status("Please run this program from administrator", True)


def on_line_edit_changed(line_edit: QLineEdit, slider: QSlider):
    str_value = line_edit.text()
    if len(str_value) > 1 and str_value[0] == '0':
        slider.setValue(int(str_value[1]))
        line_edit.setText(str_value[1])
    elif str_value == '':
        slider.setValue(0)
        line_edit.setText('0')
    elif int(str_value) > slider.maximum():
        slider.setValue(slider.maximum())
        line_edit.setText(str(slider.maximum()))
    else:
        slider.setValue(int(str_value))


def on_mode_changed():
    global mode

    if ui.solidModeRadioButton.isChecked():
        mode = Mode.SOLID
    elif ui.cycleModeRadioButton.isChecked():
        mode = Mode.CYCLE
    elif ui.breatheModeRadioButton.isChecked():
        mode = Mode.BREATHE

    print(mode)


def on_slider_value_changed(slider: QSlider, line_edit: QLineEdit):
    line_edit.setText(str(slider.value()))


def apply_clicked():
    if is_user_admin() is False:
        return

    global color, mode
    color = str(ui.colorLineEdit.text())

    if mode == Mode.SOLID:
        logitech.main([mode.value, color], set_status)

    elif mode == Mode.CYCLE:
        logitech.main([mode.value,
                       ui.cycleRateHorizontalSlider.value(),
                       ui.brightnessHorizontalSlider.value()
                       ], set_status)
    elif mode == Mode.BREATHE:
        logitech.main([mode.value, color,
                       ui.cycleRateHorizontalSlider.value(),
                       ui.brightnessHorizontalSlider.value()
                       ], set_status)


ui.applyPushButton.clicked.connect(apply_clicked)

ui.solidModeRadioButton.clicked.connect(on_mode_changed)
ui.cycleModeRadioButton.clicked.connect(on_mode_changed)
ui.breatheModeRadioButton.clicked.connect(on_mode_changed)

ui.brightnessHorizontalSlider.valueChanged.connect(lambda: on_slider_value_changed(ui.brightnessHorizontalSlider,
                                                                                   ui.brightnessLineEdit))
ui.cycleRateHorizontalSlider.valueChanged.connect(lambda: on_slider_value_changed(ui.cycleRateHorizontalSlider,
                                                                                  ui.rateLineEdit))

ui.brightnessLineEdit.textChanged.connect(lambda: on_line_edit_changed(ui.brightnessLineEdit,
                                                                       ui.brightnessHorizontalSlider))
ui.rateLineEdit.textChanged.connect(lambda: on_line_edit_changed(ui.rateLineEdit,
                                                                 ui.cycleRateHorizontalSlider))

timer.timeout.connect(clear_status)

# Run main loop    
sys.exit(app.exec_())
