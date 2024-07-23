"""
1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common 
subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string 
with some characters (can be none) deleted without changing the relative order 
f the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to 
both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

"""
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):

        t1 = len(text1)
        t2 = len(text2)

        # Step 1: Create and fill the matrix (bottom-up)
        matrix = [[0 for j in range(t2 + 1)] for i in range(t1 + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):

                if text1[i] == text2[j]:
                    matrix[i][j] = 1 + matrix[i + 1][j + 1]
                else:
                    matrix[i][j] = max(matrix[i][j + 1],matrix[i + 1][j])
        

        # Step 2: Trace back to get the LCS string (top-down)
        i, j = 0, 0
        lcs = []
        while i < t1 and j < t2:
            if text1[i] == text2[j]:
                lcs.append(text1[i])
                i += 1
                j += 1
            elif matrix[i][j + 1] > matrix[i + 1][j]:
                j += 1
            else:
                i += 1
        
        return ''.join(lcs)
    
text1 = "abcde"
text2 = "ace"
soln = Solution()
print(soln.longestCommonSubsequence(text1, text2))