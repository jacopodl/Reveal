import json
import re
from base64 import b64decode, b64encode

from reveal.handler.datahandler import DataHandler


class Jwt(DataHandler):
    def __init__(self):
        DataHandler.__init__(self, "jwt", "JSON Web Tokens encoder/decoder")

    def check(self, data):
        return data if re.fullmatch("[a-zA-Z0-9-_=]+\\.[a-zA-Z0-9-_=]+\\.[a-zA-Z0-9-_=]*", data) else None

    def decode(self, data):
        chunk = data.split(".")
        header = b64decode(Jwt.__to_std_base64(chunk[0])).decode("utf8")
        payload = b64decode(Jwt.__to_std_base64(chunk[1])).decode("utf8")
        signature = "\"\""
        if len(chunk) > 2:
            signature = (Jwt.__to_std_base64(chunk[2]))
        return "{\"Header\":%s, \"Payload\":%s, \"Signature\":\"%s\"}" % (header, payload, signature)

    def encode(self, data):
        jwt = json.loads(data)
        header = Jwt.__to_url_base64(b64encode(json.dumps(jwt["Header"]).encode("ascii")).decode("utf8"))
        payload = Jwt.__to_url_base64(b64encode(json.dumps(jwt["Payload"]).encode("ascii")).decode("utf8"))
        signature = Jwt.__to_url_base64(b64encode(json.dumps(jwt["Signature"]).encode("ascii")).decode("utf8"))
        return "%s.%s.%s" % (header, payload, signature)

    @staticmethod
    def __to_std_base64(data):
        data = data.replace("-", "+")
        data = data.replace("_", "/")
        pad = len(data) % 4
        if pad == 3:
            data += "="
        elif pad == 2:
            data += "=="
        return data

    @staticmethod
    def __to_url_base64(data):
        data = data.replace("+", "-")
        data = data.replace("/", "_")
        return data.replace("=", "")
