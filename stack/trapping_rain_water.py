"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where 
the width of each bar is 1, compute how much water it can trap 
after raining.

https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by 
array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water 
(blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""

def trap(height):

	left_max = [0] * len(height)
	right_max = [0] * len(height)

	trapped_water_height = 0

	left_max_counter = 0
	right_max_counter = 0

	#maximum height at the ith index from left side including the ith index's height
	for i in range(len(height)):
		
		left_max_counter = max(left_max_counter,height[i])
		left_max[i] = left_max_counter

	#maximum height at the ith index from right side including the ith index's height
	for i in range(len(height)-1,-1,-1):
		
		right_max_counter = max(right_max_counter,height[i])
		right_max[i] = right_max_counter


	#the trapped water will be the minimum height between left and right minus the height of the current index
	for i in range(len(height)):
		trapped_water_height = trapped_water_height + (min(left_max[i],right_max[i]) - height[i])

	return trapped_water_height

height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]

print(trap(height))