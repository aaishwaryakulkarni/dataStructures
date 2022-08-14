"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
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


	def printLinkedList(self):

		cur_node = self.head
		i = 0

		print("\n-------------------------------")
		print(f"Index : {i} | Value : {cur_node.value} <--- Head")


		while(cur_node.next != None):
			cur_node = cur_node.next
			print(f"Index : {i+1} | Value : {cur_node.value}")

			i = i + 1

	def reverseList(self):

		cur_node = self.head
		prev = None

		while cur_node:
			#so as to not lose the pointer, set temp to cur_node.next
			temp = cur_node.next
			#set cur_node.next to prev, at first it will be null
			cur_node.next = prev
			#update prev to the cur_node, as this will be the next in next iteration
			prev = cur_node
			#move the cur_node to temp
			cur_node = temp

		self.head = prev



# creating a linked list
myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(2)
myLinkedList.addAtTail(3)
myLinkedList.addAtTail(4)
myLinkedList.addAtTail(5)
myLinkedList.printLinkedList()

myLinkedList.reverseList()
myLinkedList.printLinkedList()


