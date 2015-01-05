""" Recursive fn to reverse a list """

def rec_rev(my_list) :
	if len(my_list) == 0:
		return []
	else :
		return [my_list[-1]] + rec_rev(my_list[:-1])
		

print rec_rev([1,2,3,4]) 
