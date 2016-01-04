# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def inorderTraversal_rec(root, inOrderNodes):
    if root is None:
        return inOrderNodes
    inOrderNodes = inorderTraversal_rec(root.left, inOrderNodes)
    inOrderNodes.append(root.val)
    inOrderNodes = inorderTraversal_rec(root.right, inOrderNodes)
    return inOrderNodes

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return inorderTraversal_rec(root, [])
