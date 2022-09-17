"""
In place conversion of binary tree to doubly linked list
"""

class Node:
	
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def inorder(root):
     
    if root is not None:
        inorder(root.left)
        print ("\t%d" %(root.value),end=" ")
        inorder(root.right)


class binaryTreeToDll:

	def __init__(self):
		self.head = None
		self.prev = None

	def convert(self, root):

		if root == None:
			return None

		self.convert(root.left)

		if self.prev == None:
			self.head = root

		else:
			root.left = self.prev
			self.prev.right = root

		self.prev = root

		self.convert(root.right)

		return self.head

def printList(root):
    while(root != None):
        print ("\t%d" %(root.value),end=" ")
        root = root.right

root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)

print("In-order traversal")
inorder(root)

obj = binaryTreeToDll()

head = obj.convert(root)

print("\nDLL:")
printList(head)