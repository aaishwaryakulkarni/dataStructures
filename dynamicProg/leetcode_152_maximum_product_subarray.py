"""
152. Maximum Product Subarray

Given an integer array nums, find a contiguous non-empty subarray within the array that has the 
largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 
"""

def maxProduct(nums):

	result = max(nums)

	cur_max = cur_min = 1

	for i in nums:

		if i == 0:
			cur_min = cur_max = 1
			continue

		# we are using this as cur_max is updated, so we need the original value
		temp_max = i * cur_max

		cur_max = max(i*cur_max, i*cur_min, i)
		cur_min = min(temp_max, i*cur_min, i)

		result = max(result, cur_min, cur_max)

	return result


nums = [-2,0,-1]
print(maxProduct(nums))