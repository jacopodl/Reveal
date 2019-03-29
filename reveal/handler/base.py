from reveal.handler.datahandler import DataHandler


class Base(DataHandler):
    def __init__(self, name, desc, chklen):
        DataHandler.__init__(self, name, desc)
        self.chklen = chklen

    def check(self, data):
        if isinstance(data, str):
            try:
                data = data.encode("ascii")
            except UnicodeEncodeError:
                return None
        return data if len(data) % self.chklen == 0 else None

    def encode(self, data):
        if isinstance(data, str):
            return data.encode("utf8")
        return data
