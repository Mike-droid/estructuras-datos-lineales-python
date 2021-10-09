class TwoWayNode(object):
    def __init__(self, data = None, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0


    def addSong(self, song):
        if self.head == None:
            self.head = TwoWayNode(song)
            self.tail = self.head
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = TwoWayNode(song)
            current.next.previous = current
            self.tail = current.next
        self.count += 1


    def playSongs(self):
        current = self.head
        while current != None:
            print(f'Song playing: {current.data} \n')
            current = current.next

