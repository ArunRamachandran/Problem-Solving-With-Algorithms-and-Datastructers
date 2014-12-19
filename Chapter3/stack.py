class Stack :
	""" Implementation of stack """
	def __init__(self) :
		self.items = []
	
	def is_empty(self) :
		return self.items == []

	def push(self, item) :
		self.items.append(item)

	def pop(self) :
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def size(self):
		return len(self.items)

s = Stack()
print (s.is_empty())

s.push(4)
s.push("Arun")

print (s.is_empty())
print "Peak element : %s " % (s.peek())		

s.push('True')

print "Size : %d" % (s.size())

s.push(8.4)

print "Poping elements.. "

print s.pop()
print s.pop()

print "Size : %d" % (s.size())
