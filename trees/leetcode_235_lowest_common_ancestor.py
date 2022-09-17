"""
235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given
nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
between two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”

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

def lowestCommonAncestor(root, p, q):

	cur_node = root

	while(cur_node):

		if ((p.data > cur_node.data) and (q.data > cur_node.data)):
			cur_node = cur_node.right

		elif ((p.data < cur_node.data) and (q.data < cur_node.data)):
			cur_node = cur_node.left

		else:
			return cur_node.data


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


p = TreeNode(12)
q = TreeNode(14)
print(lowestCommonAncestor(root, p, q))