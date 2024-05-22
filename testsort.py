#!/usr/bin/env python3

def off_min(input, filter=None):
	assert len(input) > 0;
	assert filter;
	
	vMin = None;
	oMin = -1;
	for o in range(0, len(input)):
		if filter and filter(input[o], o):
			continue;
		if oMin == -1 or input[o] < vMin:
			vMin = input[o];
			oMin = o;
	
	return (vMin, oMin);

def test_sort(input):
	output = [];
	
	consumed = [False] * len(input);
	is_consumed = lambda v, o: consumed[o];
	for time in range(len(input), 0, -1):
		(vMin, oMin) = off_min(input, is_consumed);
		output.append(vMin);
		consumed[oMin] = True;
	
	return output;

a = [4, 7, 1, 2, 89, 12, 3, 123, 6, 10, 0, -3, 4, -1];
print(test_sort(a));

# ./testsort.py
# [-3, -1, 0, 1, 2, 3, 4, 4, 6, 7, 10, 12, 89, 123]