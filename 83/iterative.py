# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        if curr == None:
            return curr
        while not curr.next == None:
            if curr.val != curr.next.val:
                curr = curr.next # move to the next node
            else:
                curr.next = curr.next.next # connect this node to two nodes after
        
        return head
