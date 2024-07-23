# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def  __init__(self):
        self.prev = None 

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # Store the right child of the current node
        right_child = root.right

        if self.prev:
            # Link the previous node to the current node
            self.prev.left = None
            self.prev.right = root

        # Update prev to the current node
        self.prev = root

        # Recursively flatten the left subtree
        self.flatten(root.left)

        # Recursively flatten the right subtree
        self.flatten(right_child)