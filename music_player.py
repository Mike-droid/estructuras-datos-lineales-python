from random import randint
from node_based_queue import Queue
from time import sleep

class Track:
    def __init__(self, title = None):
        self.title = title
        self.length = randint(5, 6)


class MediaPlayerQueue(Queue):
    def __init__self(self):
        super(MediaPlayerQueue, self).__init__()


    def add_track(self, track):
        self.enqueue(track)


    def play(self):
        print(f'Total songs: {self.count}')

        while self.count > 0 and self.head is not None:
            current_track = self.dequeue()
            print(f'Now playing: {current_track.title}')
            sleep(current_track.length)

