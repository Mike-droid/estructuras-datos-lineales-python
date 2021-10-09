import random

class Array:
  def __init__(self, capacity, fill_value=None):
    self.items = list()
    for _ in range(capacity):
      self.items.append(fill_value)

  def __len__(self):
    return len(self.items)


  def __str__(self):
    return str(self.items)


  def __iter__(self):
    return iter(self.items)


  def __getitem__(self, index):
    return self.items[index]


  def __setitem__(self, index, new_item):
    self.items[index] = new_item


  def __fill_array__(self):
    for i in range(len(self.items)):
      random_number = random.randrange(0, 100)
      self.items[i] = random_number


  def __sum_values__(self):
    sum = 0
    for i in range(len(self.items)):
      if type(self.items[i]) == int:
        sum += self.items[i]
    return sum

