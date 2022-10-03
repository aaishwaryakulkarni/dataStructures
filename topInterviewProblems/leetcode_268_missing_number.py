"""
"""

def missingNumber(nums):

	result = len(nums)        
	for i, n in enumerate(nums):
		result += i-n
	return result


nums = [4,5,2,1]
print(missingNumber(nums))