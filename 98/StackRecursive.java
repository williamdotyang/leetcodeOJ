/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.*;
public class Solution {
    private Stack<Integer> pushStack(TreeNode root) {
        Stack<Integer> stack = new Stack<Integer>();
        pushStack(root, stack);
        return stack;
    }
    
    private void pushStack(TreeNode root, Stack<Integer> stack) {
        if (root == null) return;
        pushStack(root.right, stack);
        stack.push(root.val);
        pushStack(root.left, stack);
    }
    
    public boolean isValidBST(TreeNode root) {
        if (root == null) return true;
        // check left child
        Stack<Integer> leftVals = pushStack(root.left);
        while (!leftVals.isEmpty()) {
            if (leftVals.pop() >= root.val) return false;
        }
        // check right child
        Stack<Integer> rightVals = pushStack(root.right);
        while (!rightVals.isEmpty()) {
            if (rightVals.pop() <= root.val) return false;
        }
        
        return isValidBST(root.left) && isValidBST(root.right);
    }
}
