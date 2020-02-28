class RingBuffer:
  def __init__(self, capacity):
    # Defineing capacity which should set limit for the number of values/elements to be added 
    self.capacity = capacity
    # Defineing current which should start index at 0
    self.current = 0
    # Defineing storage which should store added values/elements
    self.storage = [None]*capacity
    # Initial commit 

  def append(self, item):
    # If current is bigger than the setted capacity then set the current to start at index 0
    if self.current >= self.capacity:
      self.current = 0
    # Else set the storage's index at item's index 
    self.storage[self.current] = item
    # Add 1 to current's index
    self.current += 1

  def get(self):
    return [item for item in self.storage if item is not None]

buffer = RingBuffer(3)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
print(buffer.get())
# Completes MVP