"""
LeetCode

141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.
Return true if there is a cycle in the linked list. Otherwise, return false.

142. Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins. 
If there is no cycle, return null.

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


	def detect_cycle_if_exists(self):

		slow = self.head
		fast = self.head

		while(fast.next != None):
			slow = slow.next
			fast = fast.next.next

			if(slow == fast):
				return True

		return False

	def detect_cycle_start_if_exists(self):

		slow = self.head
		fast = self.head

		while(fast.next != None):
			slow = slow.next
			fast = fast.next.next

			if(slow == fast):
				start = self.head
				end = slow

				while(start != end):
					start = start.next
					end = end.next

				return start.value

		return None


# creating a linked list
myLinkedList =  MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(2)
myLinkedList.addAtTail(3)
myLinkedList.addAtTail(4)
myLinkedList.addAtTail(5)
myLinkedList.addAtTail(6)
myLinkedList.addAtTail(7)

myLinkedList.printLinkedList()

myLinkedList.create_loop()

cycle_bool = myLinkedList.detect_cycle_if_exists()
print(f"Cycle exists: {cycle_bool}")

cycle_start = myLinkedList.detect_cycle_start_if_exists()
print(f"Cycle begins at: {cycle_start}")
