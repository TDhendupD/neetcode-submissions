# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root: TreeNode, currMax: int) -> int:
            if (root.val >= currMax):
                print("if case",root.val)
                currMax = root.val
                if (root.left and root.right):
                    return helper(root.left, currMax) + helper(root.right, currMax) + 1
                elif (root.left):
                    return helper(root.left, currMax) + 1
                elif (root.right):
                    return helper(root.right, currMax) + 1
                else:
                    return 1
            else:
                print("else case", root.val)
                if (root.left and root.right):
                    return helper(root.left, currMax) + helper(root.right, currMax)
                elif (root.left):
                    return helper(root.left, currMax)
                elif (root.right):
                    return helper(root.right, currMax)
                else:
                    return 0
        if (not root.left and not root.right):
            return 1
        else:
            return helper(root, root.val)