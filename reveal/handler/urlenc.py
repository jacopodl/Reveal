import re
from urllib.parse import unquote, quote

from reveal.handler.datahandler import DataHandler


class UrlEncode(DataHandler):
    def __init__(self):
        DataHandler.__init__(self, "url", "Url encoder/decoder")

    def check(self, data):
        return data if re.search("%[a-zA-Z0-9]{2}", data) is not None else None

    def decode(self, data):
        return unquote(data)

    def encode(self, data):
        return quote(data)
