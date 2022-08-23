"""
25. Reverse Nodes in k-Group
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
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

	def getKth(self, cur, k):

		while cur and k > 0:
			cur = cur.next
			k = k - 1
		#return kth node
		return cur

	def reverseKGroup(self, head, k):

	    p = head
	    e = r = Node(None)

		# find out the length of the list
	    n = 0
	    while head:
	        head = head.next
	        n += 1

		# rearrange the nodes
	    for i in range(n // k):    # for every group
	        s = p                  # record the first node of a group that will soon become the last node of the reversed group
	        for _ in range(k):     # for every node in a group
	            t = p.next
	            p.next = e.next    # put the current node right before the head of the reversed group
	            e.next = p         # register p as the head of the reversed group
	            p = t              # visit the next node in the original list
	        e = s                  # update the end of the reversed group
	    e.next = p                 # append the tail to the end
	    self.head =  r.next


# creating a linked list [1,2,3,4,5], k = 3
linkedlist = MyLinkedList()

linkedlist.addAtHead(1)
linkedlist.addAtTail(2)
linkedlist.addAtTail(3)
linkedlist.addAtTail(4)
linkedlist.addAtTail(5)

linkedlist.printLinkedList()

res = MyLinkedList()
res.reverseKGroup(linkedlist.head, 3)
res.printLinkedList()