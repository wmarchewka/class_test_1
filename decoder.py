class Decoder:
    def __init__(self, fromwhere, **kwargs):
        self.gpio = kwargs.get("gpio",None)
        self.decoder = kwargs.get("decoder",None)
        print("From {} {} ".format(fromwhere, self.gpio ))
        print("From {} {} ".format(fromwhere, self.decoder))