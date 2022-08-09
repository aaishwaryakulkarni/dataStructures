"""

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

"""

s = 'anagram'
t = 'nagaram'

def valid_anagram(s,t):
	if((''.join(sorted(s))) == (''.join(sorted(t)))):
		return True
	else:
		return False


value_checked = valid_anagram(s,t)
print(value_checked)