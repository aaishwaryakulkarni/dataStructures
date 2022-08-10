"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

ONLY HEAD IS GIVEN, WE DONT HAVE THE LENGTH OF THE LINKED LIST

Approach:

1-2-3-4-5-6-7-8-9
n = 3, i.e. we need to delete 7

2 pointers, slow and fast at head
We first move fast by n nodes.
Slow is at head and fast is at nth node
Slow and fast are n positions apart
Now we start moving slow and fast till fast reaches end.
Now slow is at the position where we need to delete the node after slow

Steps
slow at 1, fast at 1
fast after 3 (as n=3) iterations will be at 4
slow at 2, fast at 5
slow at 3, fast at 6
slow at 4, fast at 7
slow at 5, fast at 8
slow at 6, fast at 9

fast has reached end, slow.next is to be deleted. 

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


	def delete_nth_node_from_end(self,n):

		#***********We are given only head and n************
		slow = self.head
		fast = slow

		for i in range(n):
			fast = fast.next

		while(fast.next != None):
			slow = slow.next
			fast = fast.next

		slow.next = slow.next.next




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
myLinkedList.addAtTail(9)

myLinkedList.printLinkedList()
myLinkedList.delete_nth_node_from_end(3)
myLinkedList.printLinkedList()
