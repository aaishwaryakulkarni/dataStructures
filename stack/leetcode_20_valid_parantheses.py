"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
"""

mapping = {"(": ")",
           "{": "}",
           "[": "]"}


input_str = "[{([])}]"

def check_parenthesis(input_str):

	stack = []
	for i in input_str:

		if i in mapping.keys():
			stack.append(i)
			print('pushing...')
			print(stack)
		elif i == mapping[stack[-1]]:
			stack.pop()
			print('popping...')
			print(stack)

	if stack != []:
		return False
	else:
		return True



value_checked = check_parenthesis(input_str)
print(value_checked)


