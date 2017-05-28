class LinkedList:

	def __init__(self):
		self.head = None

	def push(self, value):
		new = Node(value)
		if self.head is None:
			self.head = new
		else:
			curr = self.head
			while (curr.next is not None):
					curr = curr.next
			curr.next = new

class Node:

	def __init__(self, value):
		self.value = value
		self.next = None
