#!/usr/bin/python3
import random

def quicksort(to_be_sorted):
	print("================")
	print(to_be_sorted)
	if len(to_be_sorted) == 0:
		return []
	if len(to_be_sorted) == 1:
		return to_be_sorted
	if len(to_be_sorted) > 1:
		j = 0
		upper_limit = len(to_be_sorted)

		for i in to_be_sorted:
			if i < to_be_sorted[upper_limit - 1]:
				j += 1
		if j < upper_limit - 1:
			to_be_sorted[j], to_be_sorted[upper_limit - 1] = swap(to_be_sorted[j], to_be_sorted[upper_limit - 1])
			quicksort(to_be_sorted[:: j])
			quicksort(to_be_sorted[j + 1::])
	print("================")
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