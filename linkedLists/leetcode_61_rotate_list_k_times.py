"""
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.


Approach:

if k < length we can directly rotate it k times, but if k >= length, we need to avoid rotating unnecessary times

if length of list is 5
and k = 12, it means 5 + 5 + 2 = so we will twice rotate to the same original list and after that we will rotate 2 times.
Therefore rotating 10 times and then 2 times is a waste!
Therefore we will always do, k = k%length
This will give us the reminder which is the number of times we need to rotate the original list.

therefore, if k =12 and n = 5

k = 12%5 = 2
So we need to rotate the original list by k = 2 times.

Before doing this we will create a circular linked list by attaching last element to head.

Then we will go to the (length - k)th node. Make the  (length - k).next node head and (length - k).next = null
This will break the cycle at the kth rotation.


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

	def rotate_k_times(self, k):

		cur_node = self.head

		#calculate the length
		length = 1
		while(cur_node.next != None):
			cur_node = cur_node.next
			length = length + 1

		#make a circular linked list
		cur_node.next = self.head

		#Calculate new k
		k = k%length
		k = length - k

		#go to the new kth position and dettach the remaining list and make it head.
		for i in range(k):
			cur_node = cur_node.next

		self.head = cur_node.next
		cur_node.next = None



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

myLinkedList.rotate_k_times(20)
myLinkedList.printLinkedList()



