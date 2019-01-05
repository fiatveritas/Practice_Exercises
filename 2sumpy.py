#!/usr/bin/python3
import random #for randomizing lists

def sum_2(list_of_numbers, sum):
	look_up_table = {}

	print(look_up_table)

	for i in list_of_numbers:
		if not look_up_table:
			look_up_table[i] = i
	if list_of_numbers[0] in look_up_table:
		print("first element of list in hashtable.")
	print(look_up_table)
	return sum


if __name__ == "__main__":

	null_array = []
	array_len_one = [0]
	for i in range(10):
		random.seed(a = i)
		test_array = random.sample(range(0, 100), 10)
		print("Random list:", test_array)
		print(sum_2(test_array, 5))