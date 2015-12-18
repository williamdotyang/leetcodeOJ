# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverseList_rec(reversedList, curr):
    if curr == None:
        return curr
    if curr.next == None:
        curr.next = reversedList
        return curr
    else:
        nextNode = curr.next
        curr.next = reversedList
        return reverseList_rec(curr, nextNode)
        

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return reverseList_rec(None, head)
