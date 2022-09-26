"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

"""

def longestPalindrome(s):

	length = 0
	longest_palindrome = ""

	for i in range(len(s)):

		left = right = i

		while((left >= 0) and (right < len(s)) and (s[left] == s[right])):

			if (right - left + 1) > length:
				longest_palindrome = s[left : right + 1]
				length = right - left + 1

			left = left - 1
			right = right + 1


		left = i
		right = i + 1

		while((left >= 0) and (right < len(s)) and (s[left] == s[right])):

			if (right - left + 1) > length:
				longest_palindrome = s[left : right + 1]
				length = right - left + 1

			left = left - 1
			right = right + 1


	return longest_palindrome


s = "babbad"
print(longestPalindrome(s))