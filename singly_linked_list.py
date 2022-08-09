"""
LeetCode
707. Design Linked List

Design your implementation of the linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.

int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.

void addAtHead(int val) Add a node of value val before the first element of the linked list. 
After the insertion, the new node will be the first node of the linked list.

void addAtTail(int val) Append a node of value val as the last element of the linked list.

void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. 
If index equals the length of the linked list, the node will be appended to the end of the linked list. 
If index is greater than the length, the node will not be inserted.

void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
"""

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class MyLinkedList:
	def __init__(self):

		"""
		Initialize data structure. 
		Head and Size of the linked list

		"""

		self.head = None
		self.size = 0


	def get(self, index) -> int:

		"""
		index(int): index of the element to retrieve 
		Return -1 of index is invalid

		"""

		if ((index < 0) or (index >= self.size)):
			return -1

		#start from the head
		cur_node = self.head

		for i in range(index):
			cur_node = cur_node.next

		return cur_node.value


	def addAtHead(self, value) -> None:

		"""
		Create a new node
		new node's next will be the current head
		head will be the new node
		"""

		cur_node = self.head

		#create new node with passed value
		new_node = Node(value)

		#First link the current node at head to the new node 
		new_node.next = cur_node

		#Then make the new node the head
		self.head = new_node

		self.size = self.size + 1


	def addAtTail(self, value) -> None:

		"""
		Traverse till end
		End node's next will be new node
		"""

		new_node = Node(value)

		cur_node = self.head

		while(cur_node.next != None):
			cur_node = cur_node.next

		cur_node.next = new_node


	def addAtIndex(self, index, value) -> None:

		"""
		Traverse till index-1
		2. New node's next will be (index-1)th next
		1. (index-1)th next will be new node

		"""
		if index > self.size:
			return

		new_node = Node(value)

		cur_node = self.head

		for i in range(index - 1):
			cur_node = cur_node.next

		#new node's next will be now the current's next node
		new_node.next = cur_node.next

		#Now the current node's next will be the new node
		cur_node.next = new_node


		self.size = self.size + 1


	def printLinkedList(self):

		cur_node = self.head
		i = 0

		print("\n-------------------------------")
		print(f"Index : {i} | Value : {cur_node.value} <--- Head")


		while(cur_node.next != None):
			cur_node = cur_node.next
			print(f"Index : {i+1} | Value : {cur_node.value}")

			i = i + 1


	def deleteAtIndex(self, index) -> None:

		if ((index < 0) or (index >= self.size)):
			return

		cur_node = self.head

		if index == 0:
			self.head = cur_node.next

		else:
			for i in range(index - 1):
				cur_node = cur_node.next

			cur_node.next = cur_node.next.next


myLinkedList =  MyLinkedList()

myLinkedList.addAtHead(1)

myLinkedList.addAtTail(3)

myLinkedList.addAtIndex(1, 2)

myLinkedList.addAtHead(7)

val = myLinkedList.get(1)
print(f"Value at 1st index : {val}")     

myLinkedList.deleteAtIndex(1)  

val = myLinkedList.get(1)
print(f"Value at 1st index : {val}")    

myLinkedList.printLinkedList()