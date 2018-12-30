#!/usr/bin/python3
import random #for randomizing lists

def quicksort(to_be_sorted):
	"""this method sorts an array of unique positive numbers using
	the quicksort algorithm using the last element as a pivot."""
	if len(to_be_sorted) == 0:
		return []
	if len(to_be_sorted) == 1:
		return to_be_sorted
	if len(to_be_sorted) > 1:
		i = 0
		j = 0
		upper_limit = len(to_be_sorted)
	while j < upper_limit - 1:
		if i == j and to_be_sorted[j] < to_be_sorted[upper_limit -1]:
			i += 1
			j += 1
		elif to_be_sorted[j] > to_be_sorted[upper_limit -1]:
			j += 1
		elif to_be_sorted[j] < to_be_sorted[upper_limit -1]: # [49, 97, 53, 5, 33, 65, 62, 51, 38, 61]
			to_be_sorted[i], to_be_sorted[j] = swap(to_be_sorted[i], to_be_sorted[j])
			i += 1
			j += 1
	to_be_sorted[i], to_be_sorted[upper_limit -1] = swap(to_be_sorted[i], to_be_sorted[upper_limit -1])
	to_be_sorted[:i] = quicksort(to_be_sorted[:i])
	to_be_sorted[i:] = quicksort(to_be_sorted[i:])
	return to_be_sorted


def swap(element_1, element_2):
	"""this method swaps two elements passed into the function"""
	holder = element_1
	element_1 = element_2
	element_2 = holder
	return element_1, element_2


if __name__ == "__main__":

	null_array = []
	array_len_one = [0]

	print("Pass in an empty list.", quicksort(null_array))
	print("Pass in a list with one element.", quicksort(array_len_one))

	for i in range(10):
		random.seed(a = i)
		test_array = random.sample(range(0, 100), 10)
		print("Random list.", test_array)
		print("Sorted:", quicksort(test_array))
