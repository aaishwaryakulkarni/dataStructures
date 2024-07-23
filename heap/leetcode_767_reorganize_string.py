"""
767. Reorganize String

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.

 
Example 1:
Input: s = "aab"
Output: "aba"

Example 2:
Input: s = "aaab"
Output: ""

"""
from collections import Counter
import heapq
from multiprocessing import heap 


def reorganizeString(s):

    count = Counter(s)

    maxHeap = [[-count, char] for char, count in count.items()]
    heapq.heapify(maxHeap)

    prev = None
    res = ""

    while maxHeap or prev:

        if prev and not maxHeap:
            return ""

        #most freq, except prev
        count, char = heapq.heappop(maxHeap)

        res += char
        count += 1

        if prev:
            heapq.heappush(maxHeap, prev)
            prev = None

        if count != 0 :
            prev = [count, char]

    return res

s = "aaabbac"
print(reorganizeString(s))