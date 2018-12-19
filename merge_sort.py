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
	ordered_array = []
	import random

	random.seed(a = 2)

	left_random = random.sample(range(0, 50), 10)
	right_random = random.sample(range(0, 50), 10)
	left_size = len(left_random)
	right_size = len(right_random)
	print("Left Size:", left_size, left_random)
	print("Right Size:", right_size, right_random)
	print("xxxxxxxxxxxxxxx")

	i = 0
	j = 0
	while(i < left_size):
		while(j < right_size):
			print(i, left_random[i])
			print (j, right_random[j])
			if left_random[i] > right_random[j]:
				print("right is smaller")
				print("xxxxxxxxxxxxxxx")
				ordered_array.append(right_random[j])
				j += 1
			elif left_random[i] < right_random[j]:
				print("left is smaller")
				print("xxxxxxxxxxxxxxx")
				ordered_array.append(left_random[i])
				i += 1
			else:
				print("same size")
				print("xxxxxxxxxxxxxxx")
				ordered_array.append(left_random[i])
				ordered_array.append(right_random[j])
				i += 1
				j += 1
		if i < left_size:
			ordered_array.append(left_random[i])
			print(i, left_random[i])
			print("xxxxxxxxxxxxxxx")
			i += 1
	return ordered_array

if __name__ == '__main__':
	print(ascending_order([], []), len(ascending_order([], [])))
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