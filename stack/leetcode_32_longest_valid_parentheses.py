"""
32. Longest Valid Parentheses
Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0

"""

def longest_valid_paratheses(input_str):

	stack = []
	longest = 0

	for i in input_str:
		if i == "(":
			stack.append(i)
		else:
			if len(stack) > 0:
				stack.pop()
				longest = longest + 2

	return longest


input_str = ")()())"

print(longest_valid_paratheses(input_str))