# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        head = TreeNode(preorder[0])

        # find head in inorder:
        index = 0
        for i, v in enumerate(inorder):
            if v == preorder[0]:
                index = i
                break

        # for left tree
        left_preorder = preorder[1: index + 1]
        left_inorder = inorder[:index]
        left_tree = self.buildTree(left_preorder, left_inorder)

        # for right tree
        right_preorder = preorder[index + 1:]
        right_inorder = inorder[index + 1:]
        right_tree = self.buildTree(right_preorder, right_inorder)

        head.left = left_tree
        head.right = right_tree
        return head