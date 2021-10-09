from node import Node

circular_list = Node(None, None)
head = Node(None, None)
tail = Node(None, None)

def add_node(node):
    if circular_list.data is None:
        circular_list.data = node
        circular_list.next = circular_list
        head = circular_list
        head.data = node
        tail = circular_list
        tail.data = node
    else:
        tail = node
        tail.next = head
