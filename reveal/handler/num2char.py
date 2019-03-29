import re

from reveal.handler.datahandler import DataHandler


class Num2Char(DataHandler):
    def __init__(self):
        DataHandler.__init__(self, "n2c", "Number to char encoder/decoder")

    def check(self, data):
        return data if re.fullmatch("[\\d+,]+", data) is not None else None

    def decode(self, data):
        return "".join([chr(int(x)) for x in data.split(",")])

    def encode(self, data):
        if not isinstance(data, str):
            data = data.decode("utf8")
        return ",".join([str(ord(x)) for x in data])
