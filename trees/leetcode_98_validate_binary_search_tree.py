"""
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
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

def isvalidBST(root):

	def valid(node, left, right):

		if not node:
			return True

		if not ((node.data < right) and (node.data > left)):
			return False

		return valid(node.left, left, node.data) and valid(node.right, node.data, right)

	return valid(root, float("-inf"), float("inf"))

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

print(isvalidBST(root))