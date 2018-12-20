#!usr/bin/python3

def shrink_list(given_list):
	"""This method shrinks the
	   input list by two until
	   the list has one or no
	   elements."""

	merged_array = []

	if len(given_list) == 0:
		return []
	if len(given_list) == 1:
		return given_list
	if len(given_list) > 0:
		on_the_left = shrink_list(left_list(given_list))
		on_the_right = shrink_list(right_list(given_list))
		merged_array = ascending_order(on_the_left, on_the_right)
	return merged_array


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

	if left_array:
		left_size = len(left_array)
	else:
		left_size = 0
	if right_array:
		right_size = len(right_array)
	else:
		right_size = 0

	i = 0
	j = 0

	while(i < left_size and j < right_size):
		if left_array[i] > right_array[j]:
			ordered_array.append(right_array[j])
			j += 1
		elif left_array[i] < right_array[j]:
			ordered_array.append(left_array[i])
			i += 1
		else:
			ordered_array.append(left_array[i])
			ordered_array.append(right_array[j])
			i += 1
			j += 1
	while i < left_size:
		ordered_array.append(left_array[i])
		i += 1
	while j < right_size:
		ordered_array.append(right_array[j])
		j += 1
	return ordered_array

if __name__ == '__main__':
	import random
	random.seed(a = 0)
	dud_list = []
	zero_list = [0]
	numbers = random.sample(range(0, 100), 6)
	print("Original Input:", dud_list)
	print(shrink_list(dud_list)) #base case of zero elements
	print("Original Input:", zero_list)
	print(shrink_list(zero_list))
	print("Original Input:", numbers)
	print(shrink_list(numbers))
	print("################")
	print("################")
	print("#END OF PROGRAM#")
	print("################")
	print("################")