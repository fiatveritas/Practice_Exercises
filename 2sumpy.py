#!/usr/bin/python3
import random #for randomizing lists

def sum_2(list_of_numbers, total):
	look_up_table = {}
	counter = 0

	print("Initializing empty hashtable:", look_up_table)

	for i in list_of_numbers:
		if not look_up_table:
			look_up_table[i] = i
		if total - i not in look_up_table:
			look_up_table[i] = i
		if total - i in look_up_table:
			print (i, "+", total - i, "=", total)
			counter += 1
	print("after populating:", look_up_table)
	return counter

def check_algorithm():
	null_array = []
	array_len_one = [0]
	for i in range(10):
		print("================")
		random.seed(a = i)
		test_array = random.sample(range(0, 100), 10)
		num_1, num_2 = random.sample(test_array, 2)
		total = num_1 + num_2
		print("Random list:", test_array)
		print(sum_2(test_array, total), "pair(s) adding to", total)



if __name__ == "__main__":
	f = open('2_Sum.txt', 'r')
	lines = f.readlines()
	f.close()
	lines = [int(line) for line in lines]
	print("Min:", min(lines))
	print("Max:", max(lines))
	print("elements:", len(lines))

	#check_algorithm()
	print("================")

	
# Algorithms: Design and Analysis Part 1
# Stanford University

# Programming Question 6 - Part 1
# Count number of 2 sum variations where x + y = t
# t is any integer in interval [-10000, 10000]
# Hash table utilization problem