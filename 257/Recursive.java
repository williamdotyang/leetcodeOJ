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
    private List<String> paths;
    public List<String> binaryTreePaths(TreeNode root) {
        paths = new ArrayList<String>();
        getPaths(root, "");
        return paths;
    }
    
    private void getPaths(TreeNode root, String path) {
        if (root == null) return;
        if (root.left == null && root.right == null) {
            path += root.val;
            paths.add(path);
            return;
        }
        else 
            path += root.val + "->";
        getPaths(root.left, path);
        getPaths(root.right, path);
    }
}
