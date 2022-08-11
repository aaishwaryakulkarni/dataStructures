"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. 
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

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


	def merge(self, first, second):

		dummy = cur = Node(0)

		while(first and second):

			if first.value < second.value:
				cur.next = first
				first = first.next
			else:
				cur.next = second
				second = second.next

			cur = cur.next

		cur.next = first or second
		self.head = dummy.next


# creating a linked list
first = MyLinkedList()
second = MyLinkedList()

first.addAtHead(1)
first.addAtTail(4)
first.addAtTail(9)
first.addAtTail(10)

second.addAtHead(2)
second.addAtTail(2)
second.addAtTail(6)
second.addAtTail(11)

print("\nTwo sorted lists: ")
first.printLinkedList()
second.printLinkedList()

res = MyLinkedList()
res.merge(first.head, second.head)
print("\nMerged list: ")
res.printLinkedList()