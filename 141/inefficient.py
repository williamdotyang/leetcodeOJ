# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        head1 = head
        if not head is None:
            head2 = head.next
        else:
            head2 = None
        while not head2 is None:
            head1 = head1.next
            head2 = head2.next
            if not head2 is None:
                head2 = head2.next
            if head1 == head2:
                return True
        return False
