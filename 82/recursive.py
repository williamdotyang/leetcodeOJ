# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## @param distincts_curr Pointer to the last node in distincts
## @param curr Pointer to the current node in original linked list
## @return void
def deleteDuplicate_rec(distincts_curr, curr):
    if curr is None:
        distincts_curr.next = None
        return
    ## when curr is at the last node or it has different val with the next node,
    ## it should be added to the distincts
    if (curr.next is None) or (curr.val != curr.next.val):
        distincts_curr.next = curr
        distincts_curr = curr
        curr = curr.next
        deleteDuplicate_rec(distincts_curr, curr)
    else: 
    ## when curr has the same val with its next, jump till the node with 
    ## different val, or till the None
        val = curr.val
        while (not curr is None) and (curr.val == val):
            curr = curr.next
        deleteDuplicate_rec(distincts_curr, curr)

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fake_head = TreeNode(None)
        fake_curr = fake_head
        deleteDuplicate_rec(fake_curr, head)
        return fake_head.next
