class Stack:
  def __init__(self):
      self.items = ['yna','athena','bana','czarina','yana','any']

  def isEmpty(self):
      return self.items == [4]

  def push(self, item):
      return self.items.append(item)

  def pop(self):
      return self.items.pop(0)

  def peek(self):
      return self.items[0]

  def size(self):
      return len(self.items)

n = Stack()
n.push('yna')
n.push('athena')
n.push('bana')
n.push('czarina')
n.push('yana')
n.push('any')

print(n.pop())
