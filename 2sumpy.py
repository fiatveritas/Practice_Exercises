#!/usr/bin/python3
import random #for randomizing lists

def sum_2(list_of_numbers, total, look_up_table):
	counter = 0
	#print("Passed hashtable:", look_up_table)

	for i in list_of_numbers:
		if not look_up_table:
			look_up_table[i] = {i: False}
		if total - i not in look_up_table:
			look_up_table[i] = {i: False}
		if total - i in look_up_table:
			if look_up_table[total - i][total - i] == True:
				continue
			elif look_up_table[total - i][total - i] == False:
				print (i, "+", total - i, "=", total)
				look_up_table[total - i][total - i] = True
				look_up_table[i] = {i: True}
				counter += 1

	#print("after populating:", look_up_table)
	return counter, look_up_table

def check_algorithm():
	"""this method generates a few randomized
	   lists to test the 2sum algorithm."""
	null_array = []
	array_len_one = [0]
	for i in range(10):
		print("================")
		random.seed(a = i)
		look_up_table = {}
		test_array = random.sample(range(0, 100), 10)
		num_1, num_2 = random.sample(test_array, 2)
		total = num_1 + num_2
		print("Random list:", test_array)
		print(sum_2(test_array, total, look_up_table)[0], "pair(s) adding to", total)

def read_file():
	f = open('2_Sum.txt', 'r')
	lines = f.readlines()
	if lines:
		print("file read!")
	else:
		print("error: problem with file")
	f.close()
	return [int(line) for line in lines]

def run_2sum(list_of_numbers):
	counter = 0
	look_up_table = {}
	for t in range(-10, 11):
		print("sum:", t)
		count, look_up_table = sum_2(list_of_numbers, t, look_up_table)
		counter += count
		print("pairs:", counter)
	#print(look_up_table)
	return counter


if __name__ == "__main__":
	#list_of_numbers = read_file()
	for i in range(10):
		print("================")
		random.seed(a = i)
		test_array = random.sample(range(-10, 11), 10)
		print(test_array)
		print(run_2sum(test_array))
	#check_algorithm()
	print("================")

	
# Algorithms: Design and Analysis Part 1
# Stanford University

# Programming Question 6 - Part 1
# Count number of 2 sum variations where x + y = t
# t is any integer in interval [-10000, 10000]
# Hash table utilization problem

"""
The goal of this problem is to implement a variant of
the 2-SUM algorithm covered in this week's lectures.

The file contains 1 million integers, both positive
and negative (there might be some repetitions!).This
is your array of integers, with the ith row 
of the file specifying the ith entry of the array.

Your task is to compute the number of target values
t in the interval [-10000,10000] (inclusive) such 
that there are distinct numbers x,y in the input
file that satisfy x+y=t. (NOTE: ensuring distinctness
requires a one-line addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) 
in the space provided.
"""