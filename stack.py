from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0


    def push(self, data):
        node = Node(data, self.top)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

        self.size += 1


    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            return data
        else:
            return ("The stack is empty")


    def peek(self):
        return self.top.data if self.top else ("The stack is empty")


    def clear(self):
        while self.top:
            self.pop()


    def search_element(self, data):
        if self.top:
            current = self.top
            while current:
                if current.data == data:
                    return (f'Elemet {data} founded')
                current = current.next
            return (f'Elemet {data} not founded')
