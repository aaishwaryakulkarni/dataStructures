"""
572. Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of
root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this
node's descendants. The tree tree could also be considered as a subtree of itself.
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

def isSameTree(p, q):

	if not p and not q:
		return True

	if p and q and p.data == p.data:
		return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
	else:
		return False

def isSubTree(s, t):

	if not t:
		return True
	if not s:
		return False

	if isSameTree(s, t):
		return True

	return isSubTree(s.left, t) or isSubTree(s.right, t)


s = TreeNode(4)
s.insertNode(2)
s.insertNode(7)
s.insertNode(1)
s.insertNode(3)
s.insertNode(6)
s.insertNode(9)
s.insertNode(12)
s.insertNode(13)
s.insertNode(14)

t = TreeNode(7)
t.insertNode(6)
t.insertNode(9)


printTree(s, None, False)
printTree(t, None, False)

print(isSubTree(s, t))