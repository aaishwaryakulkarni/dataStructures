"""
2816. Double a Number Represented as a Linked List

You are given the head of a non-empty linked list representing a non-negative integer without leading 
zeroes.
Return the head of the linked list after doubling it.

 

Example 1:
Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189.
Hence, the returned linked list represents the number 189 * 2 = 378.

Example 2:
Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999.
Hence, the returned linked list reprersents the number 999 * 2 = 1998. 
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
	
	def doubleIt(self):

		def reverse(node):
			cur_node = node
			prev = None
			
			while cur_node:
				temp = cur_node.next
				cur_node.next = prev
				prev = cur_node
				cur_node = temp

			return prev
		
		reversed_list = reverse(self.head)

		carry = 0
		cur_node = reversed_list
		while cur_node:
			doubled_value = 2 * cur_node.value + carry
			cur_node.value = doubled_value % 10
			carry = doubled_value // 10
			 
			if not cur_node.next and carry:
				cur_node.next = Node(carry)
				carry = 0
				break
			cur_node = cur_node.next

		self.head = reverse(reversed_list)
		return self.head

 
# creating a linked list
myLinkedList = MyLinkedList()
myLinkedList.addAtHead(9)
myLinkedList.addAtTail(9)
myLinkedList.addAtTail(9)


myLinkedList.printLinkedList()
myLinkedList.doubleIt()
myLinkedList.printLinkedList()
