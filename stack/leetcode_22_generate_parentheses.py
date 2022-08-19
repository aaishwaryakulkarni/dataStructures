"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""

def generateParentheses(n):

	stack = []
	res = []

	def generate(open_num, close_num):

		if open_num == close_num == n:
			res.append("".join(stack))
			return

		if open_num < n:
			stack.append("(")
			generate(open_num+1, close_num)
			stack.pop()

		if close_num < open_num:
			stack.append(")")
			generate(open_num, close_num+1)
			stack.pop()

	generate(0, 0)
	return res

n = 3
print(generateParentheses(n))