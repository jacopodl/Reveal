import base64
import binascii
import re

from reveal.handler.base import Base


class B64(Base):
    def __init__(self):
        Base.__init__(self, "b64", "Base64 encoder/decoder", 4)

    def check(self, data):
        data = Base.check(self, data)
        if data is not None:
            return data if re.fullmatch(b"[A-Za-z0-9+/=]*", data) is not None else None

    def decode(self, data):
        try:
            return base64.b64decode(data)
        except binascii.Error:
            return None

    def encode(self, data):
        return base64.b64encode(Base.encode(self, data))
