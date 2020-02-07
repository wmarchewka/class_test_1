import pigpio
from rotary import Rotary
from decoder import Decoder
from digitalpots import Digitalpots
from commander import Commander
from gui import Mainwindow


class Loader:
    def __init__(self):

        self.commander = Commander("init")
        self.gpio = pigpio.pi()
        self.rotary = Rotary("init", None)
        self.decoder = Decoder("init")
        self.digitalpots = Digitalpots("init")
        self.static1 = 1
        self.mainwindow = Mainwindow(self.static1, "passing commander into mainwindow",  commander = self.commander)
        self.rotary = Rotary(self.static1, "passing gpio into rotary",  gpio = self.gpio)
        self.decoder = Decoder("passing gpio into decoder", gpio = self.gpio)
        self.static2 = 2
        self.rotary = Rotary(self.static2, "passing decoder into rotary", decoder = self.decoder)
        digitalpots = Digitalpots("passing gpio, decoder into rotary",  gpio = self.gpio, decoder = self.decoder)
        print("Local static val {}".format(self.rotary.static_val))


