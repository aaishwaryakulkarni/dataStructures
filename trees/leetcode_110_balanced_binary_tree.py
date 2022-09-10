"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

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


def isBalanced(root):

	def dfs(root):

		if not root:
			return [True, 0]

		left = dfs(root.left)
		right = dfs(root.right)

		balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)

		return [balanced, 1 + max(left[1], right[1])]

	return dfs(root)[0]


root = TreeNode(4)
root.insertNode(2)
root.insertNode(7)
root.insertNode(1)
root.insertNode(3)
root.insertNode(6)
root.insertNode(9)
root.insertNode(12)
root.insertNode(13)
# root.insertNode(14)

printTree(root, None, False)

print(isBalanced(root))
