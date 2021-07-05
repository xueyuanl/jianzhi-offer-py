# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        res = []
        if not head:
            return res

        pointer = head

        while pointer:
            res.append(pointer.val)
            pointer = pointer.next

        lens = len(res)

        # reverse the list
        for i in range(0, lens/2):
            a = res[i]
            res[i] = res[lens - 1 - i]
            res[lens - 1 - i] = a
        return res
    
    def reversePrint2(self, head):
        if not head:
            return []
        return self.reversePrint2(head.next) + [head.val]
