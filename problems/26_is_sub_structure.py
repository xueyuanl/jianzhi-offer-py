# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """

        def judge_sub_tree(a, b):
            if not b:
                return True
            if not a or a.val != b.val:
                return False

            return judge_sub_tree(a.left, b.left) and judge_sub_tree(a.right, b.right)

        if not B or not A:
            return False
        return judge_sub_tree(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
