"""
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
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

	def find_middle_element(self):

		slow = self.head
		fast = slow

		while(fast and fast.next != None):
			slow = slow.next
			fast = fast.next.next

		return slow.value


# creating a linked list
myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(2)
myLinkedList.addAtTail(3)
myLinkedList.addAtTail(4)
myLinkedList.addAtTail(5)
myLinkedList.addAtTail(6)
myLinkedList.addAtTail(7)
myLinkedList.addAtTail(8)
# myLinkedList.addAtTail(9)

myLinkedList.printLinkedList()

middle_node_value = myLinkedList.find_middle_element()
print(f"\n Middle node value : {middle_node_value}")
