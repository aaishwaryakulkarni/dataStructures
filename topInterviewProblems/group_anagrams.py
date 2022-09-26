"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
import collections

def groupAnagrams(input_list):
    ans = collections.defaultdict(list)
    print(ans)
    for s in input_list:
        ans[tuple(sorted(s))].append(s)
    print(ans)
    return ans.values()


input_list = ["eat", "tea", "tan", "ate", "nat", "bat"] 

a = groupAnagrams(input_list)
print(a)


