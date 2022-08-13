"""
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
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

	def isPalindrome(self):

		slow = self.head
		fast = slow

		#go to the middle element
		while(fast.next and fast.next.next):
			slow = slow.next
			fast = fast.next.next

		#get the second half
		second = slow.next

		#get the first half
		slow.next = None

		#reverse the second list
		prev = None
		while second:
			temp = second.next
			second.next = prev
			prev = second
			second = temp

		#first - first half of the original list
		first = self.head
		#second - second reversed half of the original list
		second = prev

		
		while(second):
			if(first.value != second.value):
				return False

			first = first.next
			second = second.next

		return True


# creating a linked list
myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(2)
myLinkedList.addAtTail(3)
myLinkedList.addAtTail(2)
myLinkedList.addAtTail(1)

myLinkedList.printLinkedList()

print(myLinkedList.isPalindrome())




