"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of
a binary tree and inorder is the inorder traversal of the same tree, construct and
return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

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


def buildTree(preorder, inorder):

	if not preorder or not inorder:
		return None

	root = TreeNode(preorder[0])
	mid = inorder.index(preorder[0])

	root.left = buildTree(preorder[1: mid + 1], inorder[: mid])
	root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])

	return root



preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = buildTree(preorder, inorder)

printTree(root, None, False)

