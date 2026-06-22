# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0
            left_node = curr.left
            right_node = curr.right

            leftDepth = dfs(left_node)
            rightDepth = dfs(right_node)

            self.res = max(self.res, leftDepth + rightDepth)

            return 1 + max(leftDepth, rightDepth)
        dfs(root)
        return self.res

        