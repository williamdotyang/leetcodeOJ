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
        ListNode tmp = reversed;
        reversed = head;
        head = head.next;
        reversed.next = tmp;
        return reverse_rec(reversed, head);
    }
}
