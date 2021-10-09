from node import Node

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0


  def append(self, data):
    node = Node(data)

    if self.tail == None and self.head == None:
      self.head = node
      self.tail = node
    else:
      current = self.tail

      while current.next:
        current = current.next

      current.next = node
      self.tail = current.next

    self.size += 1


  def size(self):
    return str(self.size)


  def iter(self):
    current = self.tail

    while current:
      value = current.data
      current = current.next
      yield value #* Genera valores pero NO los almacena


  def delete(self, data):
    current = self.tail
    previous = self.tail

    while current:
      if current.data == data:
        if current == self.tail:
          self.tail = current.next
        else:
          previous.next = current.next
          self.size -= 1
          return current.data

      previous = current
      current = current.next


  def search(self, data):
    flag = False
    for node in self.iter():
      if data == node:
        flag = True
        print(f'Data {data} found 😎')
    if not flag:
      print(f'Data {data} not found 😞')


  def clear(self):
    self.tail = None
    self.head = None
    self.size = 0


games = SinglyLinkedList()
games.append('GTA V')
print(f'head: {games.head.data} & tail: {games.tail.data}')
games.append('Fifa')
print(f'head: {games.head.data} & tail: {games.tail.data}')
games.append('Mario')
print(f'head: {games.head.data} & tail: {games.tail.data}')
