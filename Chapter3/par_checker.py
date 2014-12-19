class Stack :
	""" Class to represent a  real stack """
	def __init__(self) :
		self.items = []
	def pop(self) :
		return self.items.pop()
	def push(self, item) :
		self.items.append(item)
	def size(self) :
		return len(self.items)
	def is_empty(self) :
		return self.items == []

def par_checker(symbol_string) :
	s = Stack()
	balanced = True
	index = 0
	
	while index < len(symbol_string) and balanced :
		symbol = symbol_string[index]
		if symbol == "(" :
			s.push(symbol)
		else :
			if s.is_empty() :
				balanced = False
			else :
				s.pop()
		index = index + 1

	if balanced and s.is_empty() :
		return True
	else :
		return False

print (par_checker('((())'))
print (par_checker('(()())'))

