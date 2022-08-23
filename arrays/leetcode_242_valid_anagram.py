"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and 
false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters
exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

"""

def isAnagram(s, t):

	if len(s) != len(t):
		return False

	cS = {}
	cT = {}

	for i in range(len(s)):
		cS[s[i]] = 1 + cS.get(s[i], 0)
		cT[s[i]] = 1 + cT.get(t[i], 0)

	return cS == cT

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))