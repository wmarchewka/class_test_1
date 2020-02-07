class Commander(object):
    def __init__(self, fromwhere, **kwargs):
        self.gpio = kwargs.get("gpio", None)
        print("From {} {} ".format(fromwhere, self.gpio))
        self.decoder = kwargs.get("decoder", None)
        print("From {} {} ".format(fromwhere, self.decoder))
        self.commander = kwargs.get("commander", None)
        print("From {} {} ".format(fromwhere, self.commander))

    def parsescreen(self, value):
        print("Commander received value {}".format(value))
