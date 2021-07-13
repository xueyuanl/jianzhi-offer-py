# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        head_ = head
        previous_head = head
        if head.val == val:
            head_ = head.next
            return head_

        head = head.next

        while head:
            if head.val == val:
                previous_head.next = head.next
                break
            previous_head = head
            head = head.next

        return head_
