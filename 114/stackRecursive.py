## push the node vals in a stack, with right-most in the bottom
def pushNodesInStack(root, stack):
        if (root == None):
            return stack
        if not root.right == None:
            stack = pushNodesInStack(root.right, stack)
        if not root.left == None:
            stack = pushNodesInStack(root.left, stack)
        stack.append(root.val)
        root = None
        return stack

## recursively set the right val all the way up to root
def setRight(root, stack):
    if len(stack) == 0:
        return None
    root.left = None
    root.val = stack.pop()
    root.right = setRight(TreeNode(0), stack)
    return root
        
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        pushNodesInStack(root, stack)
        root = setRight(root, stack)
