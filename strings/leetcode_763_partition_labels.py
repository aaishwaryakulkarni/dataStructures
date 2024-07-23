"""
763. Partition Labels

You are given a string s. We want to partition the string into as many parts as possible so that each
letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant 
string should be s.

Return a list of integers representing the size of these parts.

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]

"""

def partitionLabels(s):

    #last index of each char
    last_index_dict = {}

    for i, c in enumerate(s):
        last_index_dict[c] = i

    res = []
    size, end = 0, 0
    for i, c in enumerate(s):
        size += 1

        if last_index_dict[c] > end:
            end = last_index_dict[c]

        if i == end:
            res.append(size)
            size = 0
    return res


s = "ababcbacadefegdehijhklij"
# s = "eccbbbbdec"
print(partitionLabels(s))