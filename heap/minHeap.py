"""
Max heap implementation
"""

import sys
class MinHeap:

	def __init__(self, maxsize):

		self.maxsize = maxsize
		self.size = 0
		self.heap = [0] * (self.maxsize + 1)
		self.heap[0] = -1 * sys.maxsize

	def getParent(self, position):
		return position // 2

	def getLeftChild(self, position):
		return 2 * position

	def getRightChild(self, position):
		return (2 * position) + 1

	def isLeaf(self, position):

		if ((position >= (self.size // 2)) and (position <= self.size)):
			return True
		return False

	def swap(self, position1, position2):

		self.heap[position1], self.heap[position2] = (self.heap[position2], self.heap[position1])

	def insert(self, element):

		if self.size >= self.maxsize:
			return

		self.size = self.size + 1
		self.heap[self.size] = element

		cur_node = self.size

		while(self.heap[cur_node] <  self.heap[self.getParent(cur_node)]):

			self.swap(cur_node, self.getParent(cur_node))
			cur_node = self.getParent(cur_node)

	def minHeapify(self, i):

		smallest = i
		left = self.getLeftChild(i)
		right = self.getRightChild(i)
		
		if ((left <= self.size-1) and (self.heap[left] < self.heap[smallest])):
			smallest = left

		if((right <= self.size-1) and (self.heap[right] < self.heap[smallest])):
			smallest = right

		if (smallest != i):
			self.swap(i, smallest)
			self.minHeapify(smallest)

	def minHeapFromArray(self, nums):

		self.heap = [sys.maxsize] + nums
		self.size = len(self.heap)

		for i in range(self.size//2,-1,-1):
			self.minHeapify(i)

	def printHeap(self):
		print(self.heap)


minHeap1 = MinHeap(15)
minHeap1.insert(5)
minHeap1.insert(3)
minHeap1.insert(17)
minHeap1.insert(10)
minHeap1.insert(84)
minHeap1.insert(19)
minHeap1.insert(6)
minHeap1.insert(22)
minHeap1.insert(9)
minHeap1.printHeap()

minHeap2 = MinHeap(7)
minHeap2.minHeapFromArray([10,30,50,20,35,15])
minHeap2.printHeap()