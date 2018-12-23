#!/usr/bin/python3
import math
import random

def quicksort(to_be_sorted):
	if len(to_be_sorted) == 0:
		return []
	if len(to_be_sorted) == 1:
		return to_be_sorted
	if len(to_be_sorted) > 1:
		holder = math.inf
		i = 0
		j = 0
		upper_limit = len(to_be_sorted)

		while j < upper_limit:
			if to_be_sorted[j] < to_be_sorted[upper_limit]:
				print("index:", j, "element:", to_be_sorted[j])
				j += 1
			elif to_be_sorted[j] > to_be_sorted [upper_limit]:
				print("index:", j, "element:", to_be_sorted[j])
				holder = to_be_sorted[j]
				to_be_sorted[j] = to_be_sorted[i]
				to_be_sorted[i] = holder
				i += 1
				j += 1
			#holder
	return to_be_sorted

if __name__ == "__main__":

	random.seed(a = 0)
	test_array = random.sample(range(0, 100), 10)

	print("random list", test_array)

	#null_array = []
	#array_len_one = [0]

	#print(quicksort(null_array))
	#print(quicksort(array_len_one))
	print("sorted list:", quicksort(test_array))