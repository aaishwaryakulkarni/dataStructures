"""
DFS Traversal
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

def inOrder(root):

	"""
	Inorder - Left, Root, Right
	"""
	if root:
		inOrder(root.left)
		print(root.data)
		inOrder(root.right)

def preOrder(root):

	"""
	Preorder: Root, Left, Right
	"""
	if root:
		print(root.data)
		inOrder(root.left)
		inOrder(root.right)

def postOrder(root):

	"""
	Postorder: Left, Right, Root
	"""
	if root:
		inOrder(root.left)
		inOrder(root.right)
		print(root.data)

# Tree creation
node1 = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(45)
node4 = TreeNode(22)
node5 = TreeNode(15)
node6 = TreeNode(10)
node7 = TreeNode(9)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7


printTree(node1, None, False)
print("In-order traversal:")
inOrder(node1)
print("Pre-order traversal:")
preOrder(node1)
print("Post-order traversal:")
postOrder(node1)
