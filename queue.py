class QueueError(IndexError):  # Choose base class for the new exception.
  def __init__(self, value):
    IndexError.__init__(self)
    self.value = value
    self.std = "No such index"

class Queue:
  def __init__(self):
    self.queue = []

  def put(self, elem):
    self.queue.insert(0, elem)

  def get(self):
    if len(self.queue) == 0:
      raise (QueueError("User defined error"))
    elem  = self.queue.pop(-1)
    return elem
  
  def printQueue(self):
    print(self.queue)

class SuperQueue(Queue):
  def __init__(self):
    Queue.__init__(self)
  
  def isempty(self):
    if len(self.queue) == 0:
      return True
    
    return False

  

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")