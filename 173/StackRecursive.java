/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.*;
public class BSTIterator {
    
    private Stack<Integer> stack;
    
    public BSTIterator(TreeNode root) {
        stack = new Stack<Integer>();
        pushNodesInStack(root);
    }
    
    private void pushNodesInStack(TreeNode root) {
        if (root == null) return;
        pushNodesInStack(root.right);
        stack.push(root.val);
        pushNodesInStack(root.left);
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.isEmpty();
    }

    /** @return the next smallest number */
    public int next() {
        return stack.pop();
    }
}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.hasNext()) v[f()] = i.next();
 */
