#!/usr/bin/env python3

def bubble_sort(input):
	for base_o in range(0, len(input)):
		for o in range(0, len(input) - base_o - 1):
			if input[o] > input[o + 1]:
				temp = input[o + 1];
				input[o + 1] = input[o];
				input[o] = temp;
	return input;
	# Was breaking, fixed by range(0, len(input) - base_o - 1)
	# (Use base_o to bring the upper ceiling down that's being
	# sorted up to)
	
def bubble_sort_accidental_variant(input):
	for wall_o in range(len(input), 0, -1):
		for o in range(1, wall_o):
			if input[o] < input[o - 1]:
				temp = input[o - 1];
				input[o - 1] = input[o];
				input[o] = temp;
	return input;
	# This was not insertion sort.
	
def insertion_sort(input):
	for insertee_o in range(1, len(input)):
		for o in range(insertee_o, 0, -1):
			if input[o - 1] < input[o]: break;
			temp = input[o - 1];
			input[o - 1] = input[o];
			input[o] = temp;
	return input;
	# Took a very long time to get the right incantation..
	# Holding the insertee in a variable, and continually
	# shifting things up until the insert position, was
	# not working at all. Sinking the insertee down like
	# this is better.
			
def selection_sort(input):
	for base_o in range(0, len(input)):
		min_o = base_o;
		for o in range(base_o + 1, len(input)):
			if input[o] < input[min_o]:
				min_o = o;
		temp = input[base_o];
		input[base_o] = input[min_o];
		input[min_o] = temp;
	return input;
	# Was breaking, fixed typo < input[base_o] to < input[min_o]
	# (Keep switching progressively increasing base_o with the
	# minimum that comes after it)

a = [7, 1, 2, -2, -4, 3, 12, -43, 2, 0, 8, 9, 60, 3]
print(bubble_sort(list(a)));
print(bubble_sort_accidental_variant(list(a)));
print(insertion_sort(list(a)));
print(selection_sort(list(a)));
