""" Code to construct binary digit from given integer , using stack """

class Stack:
	""" stack class corresponding to real stack """
	def __init__(self) :
		self.items = []

	def is_empty(self) :
		return self.items == []

	def push(self, item) :
		self.items.append(item)

	def pop(self) :
		return self.items.pop()

	def peek(self) :
		return self.items[len(self.items) - 1]

	def size(self) :
		return len(self.items)

def divide_by_2(dec_number) :
	rem_stack = Stack()

	print "Given Integer : %d " % (dec_number)
	while dec_number > 0 :
		rem = dec_number % 2
		rem_stack.push(rem)
		dec_number = dec_number // 2

	bin_string = ""
	while not rem_stack.is_empty():
		bin_string = bin_string + str (rem_stack.pop() )

	print "Corresponding Bin : ",
	return bin_string

print divide_by_2(42)
