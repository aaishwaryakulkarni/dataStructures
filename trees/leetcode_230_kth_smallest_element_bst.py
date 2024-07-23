"""
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed)
of all the values of the nodes in the tree.
"""
import collections

class Trunk:
    def __init__(self, prev=None, str=None):
        self.prev = prev
        self.str = str
 
def showTrunks(p):
    if p is None:
        return
    showTrunks(p.prev)
    print(p.str, end='')
 
 
def printTree(root, prev, isLeft):
    if root is None:
        return
 
    prev_str = '    '
    trunk = Trunk(prev, prev_str)
    printTree(root.right, trunk, True)
 
    if prev is None:
        trunk.str = '———'
    elif isLeft:
        trunk.str = '.———'
        prev_str = '   |'
    else:
        trunk.str = '`———'
        prev.str = prev_str
 
    showTrunks(trunk)
    print(' ' + str(root.data))
    if prev:
        prev.str = prev_str
    trunk.str = '   |'
    printTree(root.left, trunk, False)
 

class TreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def insertNode(self, data):

		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = TreeNode(data)
				else:
					self.left.insertNode(data)
			
			elif data > self.data:
				if self.right is None:
					self.right = TreeNode(data)
				else:
					self.right.insertNode(data)

		else:
			self.data = data

def kthSmallestUsingStack(root, k):
	
	stack = []
	cur_node = root

	while stack or cur_node:

		while cur_node:

			print(f"Adding to stack: {cur_node.data}")

			stack.append(cur_node)
			cur_node = cur_node.left

		cur_node = stack.pop()
		k = k -1
		print(f"Popped: {cur_node.data}")

		if k == 0:
			print("Found")
			return cur_node.data

		print(f"Going to right of: {cur_node.data}")
		cur_node = cur_node.right


class Solution:
	def kthSmallest(self, root, k):	
		self.k = k
		self.result = None
		self.found = False

		self.inOrder(root)
		return self.result

	def inOrder(self, root):
		if not root or self.found:
			return
		
		self.inOrder(root.left)
		self.k -= 1
		if self.k == 0:
			self.result = root.value
			self.found = True
			return
		self.inOrder(root.right)


root = TreeNode(4)
root.insertNode(2)
root.insertNode(7)
root.insertNode(1)
root.insertNode(3)
root.insertNode(6)
root.insertNode(9)
root.insertNode(12)
root.insertNode(13)
root.insertNode(14)

printTree(root, None, False)

k = 9
print(kthSmallestUsingStack(root, k))