import re

from reveal.handler.datahandler import DataHandler


class HexEnc(DataHandler):
    def __init__(self):
        DataHandler.__init__(self, "hex", "Hex encoder/decoder")

    def check(self, data):
        return data if re.fullmatch("[a-fA-F0-9\\s+]+", data) is not None else None

    def decode(self, data):
        try:
            return bytearray.fromhex(data)
        except ValueError:
            return None

    def encode(self, data):
        if isinstance(data, str):
            return " ".join([hex(ord(x))[2:] for x in data])
        return " ".join([hex(x)[2:] for x in data])
