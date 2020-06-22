"""
version : 1.0.0-alpha

MIT License

Copyright (c) 2019-2020 Lee Kyung-ha <i_am@nulleekh.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys
from math import pow, sqrt
from PyQt5.QtWidgets import *
from PyQt5 import uic

main_window_ui = uic.loadUiType("gui/main_window.ui")[0]
result_window_ui = uic.loadUiType("gui/result_window.ui")[0]


class MainWindow(QMainWindow, main_window_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

        self.calculateButton.clicked.connect(self.calculate_clicked)

    def calculate_clicked(self):
        second_coefficient = float(self.secondCoefficient.text())
        first_coefficient = float(self.firstCoefficient.text())
        constant = float(self.constant.text())

        if second_coefficient == 0:
            if first_coefficient == 0:
                result_0 = None
                result_1 = result_0
            else:
                result_0 = -constant / first_coefficient
                result_1 = result_0
        else:
            result_0 = (-first_coefficient + (sqrt(pow(first_coefficient, 2) - (second_coefficient * constant)))) / second_coefficient
            result_1 = (-first_coefficient - (sqrt(pow(first_coefficient, 2) - (second_coefficient * constant)))) / second_coefficient

        if result_0 is None and result_0 == result_1:
            result = "ERROR: No x in equation."
        elif result_0 == result_1:
            result = str(round(result_0, 3)) + ' (multiple root)'
        else:
            result = str(round(result_0, 3)) + ' or ' + str(round(result_1, 3))

        result_window = Result()
        result_window.represent_result(result)
        result_window.exec_()


class Result(QDialog, result_window_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Setup ui.
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        # Move window to center.
        self.doneButton.clicked.connect(self.done_clicked)
        # Call done_clicked function when done button clicked.

    def done_clicked(self):
        self.close()
        # Close window.

    def represent_result(self, result):
        self.result.setText(result)
        # Print out result data.


if __name__ == "__main__":
    application = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(application.exec_())
