"""
215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""
def findKthLargest(nums, k):
    k = len(nums) - k

    def quickSelect(l, r):
        #pivot taken is the last element and p is the first element where are going to
        #start writing if we find element less than pivot
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p = p + 1
        print(r, p, nums[r], nums[p])
        nums[r], nums[p] = nums[p], nums[r]
        print(nums)

        if p > k: return quickSelect(l, p - 1)
        elif p < k: return quickSelect(p + 1, r)
        else: return nums[p]
    
    return quickSelect(0, len(nums) - 1)

# nums = [3,2,3,1,2,4,5,5,6]
nums = [3,2,1,5,6,4]
k = 2

print(findKthLargest(nums, k))