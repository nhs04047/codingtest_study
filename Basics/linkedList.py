class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
      
class DoubleLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
      
      
linkedList = LinkedList()
linkedList.append(3)
linkedList.append(5)
linkedList.append(6)

