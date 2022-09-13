"""
Input: nums = [4,5,6,7,0,1,2]

"""
def search(nums):

	low = 0
	high = len(nums) - 1

	while low <= high:

		mid = low + ((high - low) // 2)

		if (low == high):
			return nums[low]

		if((nums[mid] < nums[mid - 1]) and (nums[mid] < nums[mid + 1])):
			return nums[mid]

		elif(nums[mid] < nums[high]):
			high = mid - 1

		else:
			low = mid + 1

nums = [4,5,6,7,0,1,2,3]

print(search(nums))