"""
647. Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 
Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""



class Solution: 

	def countSubtrings(self, s):

		result = 0

		for i in range(len(s)):

			result = result + self.addPalindrome(s, i, i)
			result = result + self.addPalindrome(s, i, i + 1)

		return result

	def addPalindrome(self, s, left, right):

		result = 0

		while((left >= 0) and (right < len(s)) and (s[left] == s[right])):

			left = left - 1
			right = right + 1

			result = result + 1

		return result


s = "aaa"

obj = Solution()

print(obj.countSubtrings(s))