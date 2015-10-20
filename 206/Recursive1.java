/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
 
// recursive approach v1 
public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode tail = head;
        if (head == null || head.next == null) {
            return head;
        }
        while (tail.next != null) {
            tail = tail.next;
        }
        reverse_rec(head, head.next);
        head.next = null;
        return tail;
    }
    
    public void reverse_rec(ListNode prev, ListNode rest) {
        if (rest.next == null) {
            rest.next = prev;
        } else {
            reverse_rec(rest, rest.next);
            rest.next = prev;
        }
    }
}
