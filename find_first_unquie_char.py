"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""

from collections import Counter

s = "loveleetcode"

dict_char = dict(Counter(s))


def find_occurence(s):

	flag = 0
	occurence_index = -1
	for i in range(len(s)):
		if flag == 0:
			occurence = dict_char[s[i]]
			if(occurence == 1):
				flag = 1
				print('Character : {} | Occurence : {} | Index : {}'.format(s[i],occurence,i))
				occurence_index = i
	return occurence_index

occurence_index = find_occurence(s)
print(occurence_index)

