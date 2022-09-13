"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.
"""

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

def diameterOfBinaryTree(root):

    diameter = 0

    def dfs(root):    

        nonlocal diameter

        if not root:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)

        diameter = max(diameter, left + right)

        return 1 + max(left, right)

    dfs(root)

    return diameter

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

print(diameterOfBinaryTree(root))
