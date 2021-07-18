# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp

        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root