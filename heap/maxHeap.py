"""
Max heap implementation
"""

import sys
class MaxHeap:

	def __init__(self, maxsize):

		self.maxsize = maxsize
		self.size = 0
		self.heap = [0] * (self.maxsize + 1)
		self.heap[0] = sys.maxsize

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

		while(self.heap[cur_node] >  self.heap[self.getParent(cur_node)]):

			self.swap(cur_node, self.getParent(cur_node))
			cur_node = self.getParent(cur_node)

	def maxHeapify(self, i):

		largest = i
		left = self.getLeftChild(i)
		right = self.getRightChild(i)
		
		if ((left <= self.size-1) and (self.heap[left] > self.heap[largest])):
			largest = left

		if((right <= self.size-1) and (self.heap[right] > self.heap[largest])):
			largest = right

		if (largest != i):
			self.swap(i, largest)
			self.maxHeapify(largest)

	def maxHeapFromArray(self, nums):

		self.heap = [sys.maxsize] + nums
		self.size = len(self.heap)

		for i in range(self.size//2,-1,-1):
			self.maxHeapify(i)

	def printHeap(self):
		print(self.heap)


maxHeap1 = MaxHeap(15)
maxHeap1.insert(5)
maxHeap1.insert(3)
maxHeap1.insert(17)
maxHeap1.insert(10)
maxHeap1.insert(84)
maxHeap1.insert(19)
maxHeap1.insert(6)
maxHeap1.insert(22)
maxHeap1.insert(9)
maxHeap1.printHeap()

maxHeap2 = MaxHeap(7)
maxHeap2.maxHeapFromArray([10,30,50,20,35,15])
maxHeap2.printHeap()
