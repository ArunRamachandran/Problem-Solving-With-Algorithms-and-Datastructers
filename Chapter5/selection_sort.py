""" More improved version of sorting, instead of exchanging the pos 
 of each element in every pass,  only one element will be shifted to
 its corresponding position in each pass. """

def selection_sort(a_list) :
	for fill_sloat in range(len(a_list) - 1, 0, -1) :
		pos_max = 0
		for location in range(1, fill_sloat + 1) :
			if a_list[location] > a_list[pos_max] :
				pos_max = location

		temp = a_list[fill_sloat]
		a_list[fill_sloat] = a_list[pos_max]
		a_list[pos_max] = temp

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(a_list)
print a_list
