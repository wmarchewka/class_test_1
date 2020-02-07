import pigpio
from rotary import Rotary
from decoder import Decoder
from digitalpots import Digitalpots

gpio = pigpio.pi()
rotary = Rotary("init")
decoder = Decoder("init")
digitalpots = Digitalpots("init")

rotary = Rotary("passing gpio into rotary", gpio = gpio)
decoder = Decoder("passing gpio into decoder", gpio = gpio)
rotary = Rotary("passing decoder into rotary", decoder = decoder)
digitalpots = Digitalpots("passing gpio, decoder into rotary",  gpio = gpio, decoder = decoder)