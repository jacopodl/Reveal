class DataHandler:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __str__(self):
        return "%s - %s" % (self.name, self.desc)

    def check(self, data):
        return None

    def decode(self, data):
        return None

    def encode(self, data):
        return None
