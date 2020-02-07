class Rotary:
    def __init__(self, static_val, fromwhere, **kwargs):

        self.gpio = kwargs.get("gpio", None)
        print("From {} {} ".format(fromwhere, self.gpio))
        self.decoder = kwargs.get("decoder", None)
        print("From {} {} ".format(fromwhere, self.decoder))
        self.commander = kwargs.get("commander", None)
        print("From {} {} ".format(fromwhere, self.commander))

        self.static_val = static_val