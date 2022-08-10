"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

ONLY HEAD IS GIVEN, WE DONT HAVE THE LENGTH OF THE LINKED LIST

Approach:

1-2-3-4-5-6-7-8-9

nth node from end- 4

2 pointers, slow and fast at head
We first move fast by n nodes.
slow is at head and fast is at nth node
slow and fast are n positions apart
now we start moving slow and fast till fast reaches end.
now slow is at the position where we need to delete the node after slow

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


	def create_loop(self):
		cur_node = self.head

		head_node = self.head

		while(cur_node.next != None):
			cur_node = cur_node.next	

		cur_node.next = head_node.next.next


	def printLinkedList(self):

		cur_node = self.head
		i = 0

		print("\n-------------------------------")
		print(f"Index : {i} | Value : {cur_node.value} <--- Head")


		while(cur_node.next != None):
			cur_node = cur_node.next
			print(f"Index : {i+1} | Value : {cur_node.value}")

			i = i + 1


	def delete_nth_node_from_end(self,n):




# creating a linked list
myLinkedList =  MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(2)
myLinkedList.addAtTail(3)
myLinkedList.addAtTail(4)
myLinkedList.addAtTail(5)
myLinkedList.addAtTail(6)
myLinkedList.addAtTail(7)
myLinkedList.addAtTail(8)
myLinkedList.addAtTail(9)

myLinkedList.printLinkedList()

