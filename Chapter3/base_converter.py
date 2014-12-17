""" more general version of divide_by_2 algorithm """
class Stack :
	def __init__(self) :
		self.items = []
	
	def is_empty(self) :
		return self.items == []

	def push(self, item) :
		self.items.append(item)

	def pop(self) :
		return self.items.pop()

	def size(self) :
		return len(self.items)

	def peek(self) :
		return self.items[len(self.items) - 1]

def base_converter(dec_number, base) :
	digits = "0123456789ABCDEF"

	rem_stack = Stack()

	print "Given Decimal No. : %d" % (dec_number)
	print " Base : %d" % (base)

	while dec_number > 0 :
		rem = dec_number % base
		rem_stack.push(rem)
		dec_number = dec_number // 2

	new_string = ""
	while not rem_stack.is_empty() :
		new_string = new_string + digits[rem_stack.pop()]

	print "Converted Value : ",
	return new_string

print base_converter(25, 2)
print base_converter(25, 16)
print base_converter(25, 8)
print base_converter(256, 16)
print base_converter(26, 26)
