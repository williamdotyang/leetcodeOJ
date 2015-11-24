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
        ListNode reversed = null;
        return reverse_rec(reversed, head);
    }
    
    public ListNode reverse_rec(ListNode reversed, ListNode head) {
        if (head == null) return reversed;
        ListNode tmp = head;
	head = head.next;
	tmp.next = reversed;
	return reverse_rec(tmp, head);
    }
}
