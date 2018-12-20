#!usr/bin/python3

def shrink_list(given_list):
	"""This method runs merge
	sorting calls on several
	defined functions."""

	merged_array = []

	if len(given_list) == 0: #base case for empty list
		return [] #must return empty, otherwise get error
	if len(given_list) == 1: #base case for when list is one length, key point
		return given_list
	if len(given_list) > 0: #base case for divide and conquer
		on_the_left = shrink_list(left_list(given_list))
		on_the_right = shrink_list(right_list(given_list))
		merged_array = ascending_order(on_the_left, on_the_right)
	return merged_array


def left_list(given_list):
	"""Creates left list by contiually
	dividing input list by two. This
	method does first half of the given
	array."""
	if int(len(given_list) / 2) > 0:
		return given_list[:int(len(given_list) / 2)]
	else:
		return []

def right_list(given_list):
	"""Creates left list by contiually
	dividing input list by two. This
	method does second half of the give
	array."""
	if int(len(given_list) / 2) > 0:
		return given_list[int(len(given_list) / 2):]
	else:
		return []			

def ascending_order(left_array, right_array):
	"""This method sorts the array by
	ascending order."""
	ordered_array = []

	if left_array:
		left_size = len(left_array)
	else: #need to hard code zero length for empty list because of error message
		left_size = 0
	if right_array:
		right_size = len(right_array)
	else: #need to hard code zero length for empty list because of error message
		right_size = 0

	i = 0
	j = 0

	while(i < left_size and j < right_size): #indices run until out of bounds
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
	while i < left_size: #activates if one of the lists goes through its elements soon
		ordered_array.append(left_array[i])
		i += 1
	while j < right_size: #activates if one of the lists goes through its elements soon
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