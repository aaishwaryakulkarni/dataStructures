"""
703. Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream. Note that it is the 
kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the 
stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element 
representing the kth largest element in the stream.
 
Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8


Approach:

We first heapify the given array 4,5,8,2
As we do this the maximum will be the root
We need the kth largest element
If we have k elements in the min heap, the root node will 
be the kth largest element

So we pop till len of maxheap is <= k
We can return the min in O(1).

As we add a new element we again pop once so we have again the kth
largest at the root node.

"""

import heapq

class KthLargest:

	def __init__(self, k, nums):

		self.maxHeap = nums
		self.k = k

		heapq.heapify(self.maxHeap)

		while len(self.maxHeap) > k:
			heapq.heappop(self.maxHeap)
        
	def add(self, val):

		heapq.heappush(self.maxHeap, val)

		while len(self.maxHeap) > k:
			heapq.heappop(self.maxHeap)

		return self.maxHeap[0]


k = 3
nums = [4, 5, 8, 2]
obj = KthLargest(k, nums)
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))