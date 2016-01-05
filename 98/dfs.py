# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfsPush(root, visited):
    if root is None:
        return visited
    dfsPush(root.left, visited)
    visited.append(root.val)
    dfsPush(root.right, visited)
    return visited

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ordered = dfsPush(root, [])
        for i in range(1, len(ordered)):
            if ordered[i] <= ordered[i-1]:
                return False
        return True

