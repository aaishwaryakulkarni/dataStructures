"""
137. Single Number II

Given an integer array nums where every element appears three times except for one, which appears exactly once. 
Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99
 
"""

def singleNumber(nums):
    ones, twos = 0, 0

    for n in nums:
        ones = (ones ^ n) & ~twos
        twos = (twos ^ n) & ~ones
    
    return ones


nums = [2,2,3,2]
nums = [5, 5, 5, 6, 4, 4, 4]
print(singleNumber(nums))
