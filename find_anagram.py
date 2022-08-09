"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""

s = "cbaebabacd"
p = "abc"

# s = "abab" 
# p =  "ab"

length_of_p = len(p)

for i in range(len(s)):
	check_string = s[i:length_of_p]
	if(len(check_string) == len(p)):
		if (''.join(sorted(p)) == ''.join(sorted(check_string))):
			print('Anagram present from index: ',i)

	length_of_p = length_of_p + 1

	