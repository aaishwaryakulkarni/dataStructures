"""
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in 
the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only 
constant extra space.

All the integers in nums appear only once except for precisely one integer which 
appears two or more times.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3


Approach:
index 0 1 2 3 4
value 1 3 4 2 2

Consider value as a pointer
1 points at 1 
3 points at pos 3
"""