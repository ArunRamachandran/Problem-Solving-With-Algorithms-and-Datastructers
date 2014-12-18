def pal(string) :
	my_list =  list(string)
	if len(my_list) == 1:
		#print "Yeah... len : 1, True"
		return True
	elif len(my_list) == 2:
		if my_list[0] == my_list[1]:
			return True
		else :
			return False
	else :
		l = len(my_list)
		print "my_list[0] : %c" % (my_list[0])
		print "my_list[l - 1] : %c" % (my_list[l - 1])
		if my_list[0] != my_list[l - 1]:
			return False
		else :
			my_list = my_list[1 : l - 1]
			my_string = ''.join(my_list)
	pal(my_string)

case = pal("radar")
if case == True:
	print True
else :
	print False

