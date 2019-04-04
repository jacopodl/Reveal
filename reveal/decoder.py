from reveal.handler.datahandler import DataHandler
from reveal.node import Node


def ensure_string(string):
    if string is None:
        return None

    if not isinstance(string, str):
        try:
            return string.decode("utf8")
        except UnicodeDecodeError:
            return None
    return string


class DataTransformation:
    def __init__(self):
        self.handlers = {}

    def add_handler(self, handler):
        if isinstance(handler, DataHandler):
            self.handlers[handler.name] = handler
            return
        raise TypeError("invalid handler")

    def available_decoders(self):
        return [(handler.name, handler.desc) for handler in self.handlers.values()]

    def decode(self, data, limits=24):
        head = Node(data, None)
        queue = [head]
        idx = 0

        while queue and limits > 0:
            for i in range(len(queue)):
                nodes = self.__decode__(queue[i])
                if nodes:
                    queue += nodes
                idx += 1
            queue = queue[idx:]
            limits -= 1
            idx = 0

        return head

    def __decode__(self, node):
        nwnodes = []
        found = False

        for handler in self.handlers.values():
            tmp = handler.check(node.data)
            if tmp is not None:
                tmp = ensure_string(handler.decode(tmp))
                if tmp is not None:
                    found = True
                    ns = Node(tmp, handler)
                    node.append_child(ns)
                    nwnodes.append(ns)

        if not nwnodes and found:
            if node.parent is not None:
                node.parent.delete_child(node)

        return nwnodes

    def encode(self, data, transformations):
        for trans in transformations:
            if trans not in self.handlers:
                raise NameError("invalid encoder: %s" % trans)
            data = self.handlers[trans].encode(data)
        if not isinstance(data, str):
            data = data.decode("utf8")
        return data
