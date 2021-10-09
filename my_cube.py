import random

class Cube:
  def __init__(self, length, fill_value=None):
    self.length = length
    self.cube = [[[fill_value for z in range(length)] for y in range(length)] for x in range(length)]


  def fill_cube(self):
    for x in range(self.length):
      for y in range(self.length):
        for z in range(self.length):
          self.cube[x][y][z] = random.randint(1, 100)

