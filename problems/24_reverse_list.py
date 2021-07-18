# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    # what a shit did I write
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        pre = head
        if head.next:
            cur = head.next
            net = head.next
        else:
            return head

        if head.next.next:
            net = net.next
        else:
            pre.next = None
            cur.next = pre
            return cur

        pre.next = None
        cur.next = pre
        while net:
            pre = cur
            cur = net
            net = net.next
            cur.next = pre
        return cur






