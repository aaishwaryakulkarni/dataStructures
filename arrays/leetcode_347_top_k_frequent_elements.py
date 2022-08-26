"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent 
elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Follow up: Your algorithm's time complexity must be better than 
O(n log n), where n is the array's size.

"""

def topKFrequent(nums, k):

	count_dict = {}
	frequency = [[] for i in range(len(nums) + 1)]

	#{1: 3, 2: 2, 3: 1}
	for i in nums:
		count_dict[i] = 1 + count_dict.get(i, 0)

	# 0    1    2    3   4   5   6
	#[[], [3], [2], [1], [], [], []]
	#insert at ith index (ith index is the count of a number, there can be multiple so its a list)
	for key, value in count_dict.items():
		frequency[value].append(key)

	result = []
	for i in range(len(frequency)-1, 0, -1):

		for n in frequency[i]:
			result.append(n)

			if len(result) == k:
				return result

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))