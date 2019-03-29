import base64
import binascii
import re

from reveal.handler.base import Base


class B32(Base):
    def __init__(self):
        Base.__init__(self, "b32", "Base32 encoder/decoder", 8)

    def check(self, data):
        data = Base.check(self, data)
        if data is not None:
            return data if re.fullmatch(b"[A-Z2-7=]*", data) is not None else None

    def decode(self, data):
        try:
            return base64.b32decode(data)
        except binascii.Error:
            return None

    def encode(self, data):
        return base64.b32encode(Base.encode(self, data))
