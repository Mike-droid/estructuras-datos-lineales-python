class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class TwoWayNode(Node):
    def __init__(self, data, previous = None, next = None):
        Node.__init__(self, data, next)
        self.previous = previous


    def add_after(self, node):
        node = TwoWayNode(node)
        if self.next == None:
            self.next = node
            node.previous = self
        else:
            probe = self
            while probe.next != None:
                probe = probe.next
            probe.next = node
            node.previous = probe


    def find_node(self, data):
        if self.data == data:
            return (f'Se ha encontrado {self.data}')
        elif self.next == None:
            return (f'No existe ese dato')
        else:
            return self.next.find_node(data)
