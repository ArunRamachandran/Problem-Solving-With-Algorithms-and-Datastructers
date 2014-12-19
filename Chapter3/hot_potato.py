""" A real time implementation of modern - day equivalent of the famous
Josephus Problem. """

class Queue :
	""" Defining a Queue.. With FIFO logic"""
	def __init__(self) :
		self.items = []

	def is_empty(self) :
		return self.items == []

	def enqueue(self, item) :
		self.items.insert(0, item)

	def dequeue(self) :
		return self.items.pop()

	def size(self) :
		return len(self.items)

def hot_potato(name_list, num) :
	""" Will accept a list of names and a constant number """
	sim_queue = Queue()
	for name in name_list:
		sim_queue.enqueue(name)

	while sim_queue.size() > 1 :
		for i in range(num) :
			sim_queue.enqueue(sim_queue.dequeue())

		sim_queue.dequeue()

	return sim_queue.dequeue()

print hot_potato(["Bill", "David", "Susan", "jane", "Kent", "Brad"], 7)
	
