#!/usr/bin/python3
import random

def quicksort(to_be_sorted):
	print("================")
	print("to be sorted", to_be_sorted)
	if len(to_be_sorted) == 0:
		return []
	if len(to_be_sorted) == 1:
		return to_be_sorted
	if len(to_be_sorted) > 1:
		i = 0
		j = 0
		upper_limit = len(to_be_sorted)
	#print("================")
	while j < upper_limit - 1:
		#print("i", i)
		#print("j", j)
		#print("list at start of iteration:", to_be_sorted)
		if i == j and to_be_sorted[j] < to_be_sorted[upper_limit -1]:
			i += 1
			j += 1
		elif to_be_sorted[j] > to_be_sorted[upper_limit -1]:
			j += 1
		elif to_be_sorted[j] < to_be_sorted[upper_limit -1]: # [49, 97, 53, 5, 33, 65, 62, 51, 38, 61]
			to_be_sorted[i], to_be_sorted[j] = swap(to_be_sorted[i], to_be_sorted[j])
			i += 1
			j += 1
		#print("list after iteration:", to_be_sorted)
		#print("================")
	to_be_sorted[i], to_be_sorted[upper_limit -1] = swap(to_be_sorted[i], to_be_sorted[upper_limit -1])
	#print("list before recursion:", to_be_sorted)
	#print("================")
	to_be_sorted[:i] = quicksort(to_be_sorted[:i])
	to_be_sorted[i:] = quicksort(to_be_sorted[i:])
	return to_be_sorted


def swap(element_1, element_2):
	holder = element_1
	element_1 = element_2
	element_2 = holder
	return element_1, element_2


if __name__ == "__main__":

	random.seed(a = 0)
	test_array = random.sample(range(0, 100), 10)

	print("random list:", test_array)

	#null_array = []
	#array_len_one = [0]

	#print(quicksort(null_array))
	#print(quicksort(array_len_one))
	print("sorted list:", quicksort(test_array))
	print("orginal:", test_array)
	# [49, 97, 53, 5, 33, 65, 62, 51, 38, 61]