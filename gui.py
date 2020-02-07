import signal
import sys
from commander import Commander

from PySide2.QtUiTools import QUiLoader
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QTimer, QFile, QObject
from PySide2.QtGui import QFontDatabase
from PySide2.QtWidgets import QTableWidgetItem


class Mainwindow(QObject):

    def __init__(self, static_val, fromwhere, **kwargs):
        super().__init__()

        self.gpio = kwargs.get("gpio", None)
        print("From {} {} ".format(fromwhere, self.gpio))
        self.decoder = kwargs.get("decoder", None)
        print("From {} {} ".format(fromwhere, self.decoder))
        self.commander = kwargs.get("commander", None)
        print("From {} {} ".format(fromwhere, self.commander))
        self.loadscreen()
        self.exit_signalling()
        self.signal_and_slots()

    def exit_signalling(self):
        signal.signal(signal.SIGINT, self.exit_application)
        signal.signal(signal.SIGTERM, self.exit_application)

    def loadscreen(self):
        try:
            self.guiname = "mainwindow.ui"
            ui_file = QFile(self.guiname)
            ui_file.open(QFile.ReadOnly)

            loader = QUiLoader()
            self.window = loader.load(ui_file)
            ui_file.close()

            self.window.show()
            print('Loading screen ' + self.guiname)

        except FileNotFoundError:
            print("Could not find {}".format(self.guiname))  # CATCHES EXIT SHUTDOWN

    def signal_and_slots(self):
        self.window.PB_1.clicked.connect(self.commander.parsescreen)   #self.)

    def exit_application(self, signum, frame):
        print("Starting shutdown")
        print("Received signal from signum: {} with frame:{}".format(signum, frame))
        sys.exit(0)
