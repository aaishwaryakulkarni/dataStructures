"""
1721. Swapping Nodes in a Linked List

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node 
from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
"""


class Node:

	def __init__(self, value):
		self.next = None
		self.value = value


class MyLinkedList:

	def __init__(self):
		self.head = None
		self.size = 0


	def addAtHead(self, value):

		cur_node = self.head

		new_node = Node(value)

		new_node.next = cur_node

		self.head = new_node

		self.size += 1

	def addAtTail(self, value):

		new_node = Node(value)

		cur_node = self.head

		while cur_node.next:
			cur_node = cur_node.next

		cur_node.next = new_node

	def printLinkedList(self):

		cur_node = self.head
		i = 0

		print("\n-------------------------------")
		print(f"Index : {i} | Value : {cur_node.value} <--- Head")


		while(cur_node.next != None):
			cur_node = cur_node.next
			print(f"Index : {i+1} | Value : {cur_node.value}")

			i = i + 1

	def swapNodes(self, k):

		slow = fast = self.head

		for _ in range(k-1):
			fast = fast.next

		swap1 = fast

		while fast.next:
			slow = slow.next
			fast = fast.next

		swap2 = slow

		swap1.value, swap2.value = swap2.value, swap1.value



# creating a linked list
myLinkedList =  MyLinkedList()
myLinkedList.addAtHead(7)
myLinkedList.addAtTail(9)
myLinkedList.addAtTail(6)
myLinkedList.addAtTail(6)
myLinkedList.addAtTail(7)
myLinkedList.addAtTail(8)
myLinkedList.addAtTail(3)
myLinkedList.addAtTail(0)
myLinkedList.addAtTail(9)
myLinkedList.addAtTail(5)

myLinkedList.swapNodes(5)

myLinkedList.printLinkedList()