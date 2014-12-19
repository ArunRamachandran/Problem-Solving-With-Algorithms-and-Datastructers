class Stack :
	""" Implementation of stack """
	def __init__(self) :
		self.items = []
	
	def is_empty(self) :
		return self.items == []

	def push(self, item) :
		self.items.insert(0, item)

	def pop(self) :
		return self.items.pop(0)

	def peek(self):
		return self.items[0]

	def size(self):
		return len(self.items)

s = Stack()
"""
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

print s.is_empty()

s.push('hello')
s.push('world')
s.push('My world')

print "Poping.."
print s.pop() """

s.push('x')
s.push('y')
s.pop()
s.push('z')
print "peek : ",
print s.peek()
