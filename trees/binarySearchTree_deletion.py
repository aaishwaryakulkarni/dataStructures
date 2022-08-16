"""
Binary Tree
1. Each node has atmost 2 children
2. Node's left child's value is less than its parent's value
3. Node's right child's value is greater than its parent's value

Deletion logic:

Case1:
If the node to be deleted is a leaf node, simply delete this node.

Case2:
If the node to be deleted has a single child, replace the node with the 
child's value and remove the child node from the tree.

Case3:
If the node to be deleted has 2 children
Get the inorder successor of the node
Replace the node to be deleted with this node
Remove the inorder successor from the tree.

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

def minValueNode(node):
    current = node
  
    while(current.left is not None):
        current = current.left
  
    return current

def deleteNode(root, data):

    if root is None:
        return root

    if data < root.data:
        root.left = deleteNode(root.left, data)
    
    elif data > root.data:
        root.right = deleteNode(root.right, data)

    else:

        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        print(temp.data)

        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)

    return root





root = TreeNode(27)
root.insertNode(14)
root.insertNode(35)
root.insertNode(31)
root.insertNode(10)
root.insertNode(19)

printTree(root, None, False)

deleteNode(root, 14)

printTree(root, None, False)