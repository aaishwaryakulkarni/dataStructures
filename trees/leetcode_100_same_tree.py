"""
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same
or not.

Two binary trees are considered the same if they are structurally identical, and the nodes
have the same value.

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


p = TreeNode(4)
p.insertNode(2)
p.insertNode(7)
p.insertNode(1)
p.insertNode(3)
p.insertNode(6)
p.insertNode(9)
p.insertNode(12)
p.insertNode(13)
p.insertNode(14)

q = TreeNode(4)
q.insertNode(2)
q.insertNode(7)
q.insertNode(1)
q.insertNode(3)
q.insertNode(9)
q.insertNode(12)
q.insertNode(13)
q.insertNode(14)

printTree(p, None, False)
printTree(q, None, False)

print(isSameTree(p, q))