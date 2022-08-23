"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly 
once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

"""

import collections

def groupAnagrams(input_list):

    ans = collections.defaultdict(list)

    for i in input_list:

    	count = [0] * 26

    	for char in i:
    		count[ord(char) - ord("a")] += 1

    	ans[tuple(count)].append(i)

    return list(ans.values())

input_list = ["eat", "tea", "tan", "ate", "nat", "bat"] 
print(groupAnagrams(input_list))