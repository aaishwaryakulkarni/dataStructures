"""
84. Largest Rectangle in Histogram
Given an array of integers heights representing the histogram's 
ar height where the width of each bar is 1, return the area of 
the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar 
is 1.
The largest rectangle is shown in the red area, which has an 
area = 10 units.
"""


def largestRectangleArea(heights):
	max_area = 0
	stack = []

	for index, height in enumerate(heights):
		start = index

		while stack and stack[-1][1] > height:

			i, h = stack.pop()
			max_area = max(max_area, h * (index - i))

			#As the index we just popped is greater in height we can extend the index to that
			start = i

		stack.append((start,height))

	for index, height in stack:
		max_area = max(max_area, height * (len(heights) - index))

	return max_area



heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))
