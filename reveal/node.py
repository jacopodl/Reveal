class Node:
    def __init__(self, data, handler):
        self.data = data
        self.handler = handler
        self.parent = None
        self.child = []

    def __eq__(self, other):
        return self.data == other.data and self.handler.name == other.handler.name

    def append_child(self, child):
        if isinstance(child, Node):
            child.parent = self
            self.child.append(child)
            return
        raise TypeError("invalid child")

    def delete_child(self, child):
        if self.child:
            self.child.remove(child)
        if self.parent is not None and not self.child:
            self.parent.delete_child(self)
        return child
