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
	"""this method generates a few randomized
	   lists to test the 2sum algorithm."""
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
	for t in xrange(-10000, 10001):
		counter += sum_2(list_of_numbers)
		print(counter)


if __name__ == "__main__":
	list_of_numbers = read_file()
	#run_2sum(list_of_numbers)
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