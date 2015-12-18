/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
 
public class Solution {
    public ListNode reverseList(ListNode head) {
        return reverse_rec(null, head);
    }
    
    public ListNode reverse_rec(ListNode reversed, ListNode head) {
        if (head == null) return reversed;
	ListNode next = head.next;
	head.next = reversed;
	return reverse_rec(head, next);
    }
}
