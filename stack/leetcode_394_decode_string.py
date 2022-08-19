"""
394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the 
square brackets is being repeated exactly k times. Note that k is guaranteed 
to be a positive integer.

You may assume that the input string is always valid; there are no extra 
white spaces, square brackets are well-formed, etc. Furthermore, you may 
assume that the original data does not contain any digits and that digits 
are only for those repeat numbers, k. For example, there will not be input 
like 3a or 2[4].

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Approach:

----------------------------
num = 2

if char == "[" then
append in stack
stack = ["",2]

if char == "]" then
pop from stack
opstring = "" + 2(abc)

else--
opstring = "abc"

------------------------------
num = 3

if char == "[" then
append in stack
stack = ["abcabc",3]

if char == "]" then
pop from stack "abcabc" and 3
opstring = "abcabc" + 3(cd)

else--
opstring = "cd"

------------------------------
"""

def decodeString(s):

	num = 0
	op_string = ""
	stack = []

	for char in s:

		if char.isdigit():
			num = num*10 +int(char)

		elif char == "[":
			stack.append(op_string)
			stack.append(num)
			op_string = ""
			num = 0

		elif char == "]":
			num_multiply = stack.pop()
			prev_string = stack.pop()
			op_string = prev_string + num_multiply*op_string

		else:
			op_string = op_string + char

	return op_string
			
s = "2[abc]3[cd]ef"
print(decodeString(s))
