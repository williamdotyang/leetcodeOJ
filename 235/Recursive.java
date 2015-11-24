/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (p.val > q.val) {
            TreeNode temp = q;
            q = p;
            p = temp;
        }
            
        if (p.val <= root.val && root.val <= q.val) return root;
        if (root.val < p.val) return lowestCommonAncestor(root.right, p, q);
        else return lowestCommonAncestor(root.left, p, q);
    }
}
