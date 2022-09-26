"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

def longestCommonPrefix(strs):

	result = ""

	for i in range(len(strs[0])):
		print("-------------------------")
		for s in strs:
			print(s[i],strs[0][i])

			if i == len(s) or s[i] != strs[0][i]:
				return result

		result = result + strs[0][i]
		print(f"Result : {result}")

	return result


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))