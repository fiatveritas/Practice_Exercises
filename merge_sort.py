#!usr/bin/python3

def shrink_list(given_list):
	"""This method shrinks the
	   input list by two until
	   the list has one or no
	   elements."""

	if len(given_list) == 0:
		print("Length zero list.", given_list)
		return []
	if len(given_list) == 1:
		print("Length one list.", given_list)
		return given_list
	if len(given_list) > 0:
		print("Length:", len(given_list), "Reduced List:", given_list)
		on_the_left = shrink_list(left_list(given_list))
		print("Left:", on_the_left)
		on_the_right = shrink_list(right_list(given_list))
		print("Right:", on_the_right)

def left_list(given_list):
	if int(len(given_list) / 2) > 0:
		return given_list[:int(len(given_list) / 2)]
	else:
		return []

def right_list(given_list):
	if int(len(given_list) / 2) > 0:
		return given_list[int(len(given_list) / 2):]
	else:
		return []			

def ascending_order(left_array, right_array):
	import random

	random.seed(a = 0)

	left_random = random.sample(range(0, 50), 10)
	right_random = random.sample(range(0, 50), 10)
	left_size = len(left_random)
	right_size = len(right_random)
	print("Left Size:", left_size, left_random)
	print("Right Size:", right_size, right_random)
	return []

if __name__ == '__main__':
	print(ascending_order([], []))
	#dud_list = []
	#zero_list = [0]
	#numbers = [i for i in range(9, 0, -1)]
	#print("Original Input:", numbers)
	#shrink_list(dud_list) #base case of zero elements
	#shrink_list(zero_list)
	#shrink_list(numbers)
	'''	print("################")
	print("################")
	print("#END OF PROGRAM#")
	print("################")
	print("################")'''