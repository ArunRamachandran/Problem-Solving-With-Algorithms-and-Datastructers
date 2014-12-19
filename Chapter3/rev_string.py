""" Write a fn rev_string(my_str) that uses a stack to reverse the 
characters in a string. """

class Stack:
	""" class stack to implement a stack operations """
	def __init__(self) :
		self.items = []
		my_list = []

	def pop(self):
		return self.my_list.pop()
	
	def str_to_list(self, my_str) :
		self.my_list = list(my_str)
	
	def push(self, item) :
		self.items.append(item)

	"""def pick_elements(self) :
		l = len(self.my_list)
		while l > 0 :
			items = self.my_list.pop()
		print "Items : ",
		print self.items	"""

def rev_string() :
	s = Stack()
	my_str = raw_input('Give a string ? ')
	s.str_to_list(my_str)
	print "My_list : ",
	print s.my_list
	l = len(s.my_list)
	print "Length : ",
	print l
	while l > 0:
		s.push(s.pop())
		l = l - 1

	print "String in reversed Order : ",

	print ''.join(s.items)

rev_string()
	
	
