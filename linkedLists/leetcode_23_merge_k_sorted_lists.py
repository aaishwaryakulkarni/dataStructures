"""
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

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

	def merge2Lists(self, l1, l2):

		dummy = cur = Node(0)

		while l1 and l2:
			if l1.value < l2.value:
				cur.next = l1
				l1 = l1.next

			else:
				cur.next = l2
				l2 = l2.next

			cur = cur.next

		cur.next = l1 or l2

		return dummy.next

	def mergeKLists(self, lists):

		if not lists or len(lists) == 0:
			return None

		while len(lists) > 1:

			internalLists = []

			for i in range(0, len(lists), 2):

				l1 = lists[i]

				l2 = None
				if (i + 1) < len(lists):
					l2 = lists[i + 1]

				internalLists.append(self.merge2Lists(l1, l2))

			lists = internalLists

		self.head = lists[0]


# creating a linked list [[1,4,5],[1,3,4],[2,6]]
first = MyLinkedList()
second = MyLinkedList()
third = MyLinkedList()

first.addAtHead(1)
first.addAtTail(4)
first.addAtTail(5)

second.addAtHead(1)
second.addAtTail(3)
second.addAtTail(4)
second.addAtTail(11)

third.addAtHead(2)
third.addAtTail(6)


print("\nSorted lists: ")
first.printLinkedList()
second.printLinkedList()
third.printLinkedList()

res = MyLinkedList()
res.mergeKLists([first.head, second.head, third.head])
res.printLinkedList()