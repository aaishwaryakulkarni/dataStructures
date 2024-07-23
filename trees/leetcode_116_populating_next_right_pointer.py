"""
116. Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.


Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


Example 2:
Input: root = []
Output: []
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
    if root.next:
        print(f' {str(root.data)}({str(root.next.data)})')
    else:
        print(f' {str(root.data)}(None)')
    if prev:
        prev.str = prev_str
    trunk.str = '   |'
    printTree(root.left, trunk, False)
 

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None


def connectBfs(root):
     
    q = collections.deque()

    if root:
        q.append(root)

    while q:
        qlen = len(q)

        for i in range(qlen):
            node = q.popleft()

            if i < qlen-1:
                node.next = q[0]

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            
    return root

def connectO1(root):
     
	cur, next = root, root.left if root.left else None

	while cur and next:
		cur.left.next = cur.right
		if cur.next:
			cur.right.next = cur.next.left

		cur = cur.next
		if not cur:
			cur = next
			next = cur.left
            
	return root

             

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

printTree(root, None, False)

# connectBfs(root)
connectO1(root)
printTree(root, None, False)
