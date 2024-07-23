"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

"""
from collections import Counter

class Solution(object):
    def minWindow(self, s, t):

        #base condition
        if t == "":
            return ""
        
        window = {}
        target = Counter(t)
        
        have, need = 0 , len(target)
        res, resLen = [-1, -1], float("infinity")
        left, right = 0, 0

        while right < len(s):

            character = s[right]

            #expanding window to right
            window[character] = window.get(character,  0) + 1

            if character in target and window[character] == target[character]:
                have += 1
            
            #found a substring
            while have == need:

                #update the minimum window substring
                if(right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                
                #contracting window from left
                window[s[left]] -= 1
                if s[left] in target and window[s[left]] < target[s[left]]:
                    have -= 1
                
                left += 1
            
            right += 1

        start_index, end_index  = res
        return s[start_index: end_index + 1] if resLen != float("infinity") else ""        


s = "ADOBECODEBANC"
t = "ABC"

soln = Solution()
print(soln.minWindow(s,t))