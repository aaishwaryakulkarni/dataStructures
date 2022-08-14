"""
2. Add Two Numbers


You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


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


	def addTwoNumbers(self, first, second):

		dummy = cur = Node(0)
		carry = 0

		while(first or second or carry):

			if first:
				carry = carry + first.value
				first = first.next

			if second:
				carry = carry + second.value
				second = second.next

			cur.next = Node(carry%10)
			cur = cur.next
			carry = carry//10

		self.head = dummy.next


# creating a linked list
first = MyLinkedList()
second = MyLinkedList()

first.addAtHead(2)
first.addAtTail(4)
first.addAtTail(3)

second.addAtHead(5)
second.addAtTail(6)
second.addAtTail(4)

print("\nTwo numbers to add (in reverse):")
first.printLinkedList()
second.printLinkedList()

res = MyLinkedList()
res.addTwoNumbers(first.head, second.head)
print("\nAddition (in reverse):")
res.printLinkedList()



