# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function returns a list: [is_balanced (bool), height (int)]
        def dfs(curr: Optional[TreeNode]) -> list:
            # Base Case: An empty tree is balanced and has a height of 0
            if not curr:
                return [True, 0]
            
            # 1. Ask the left subtree for its balance status and height
            left = dfs(curr.left)
            # 2. Ask the right subtree for its balance status and height
            right = dfs(curr.right)
            
            # A node is balanced if:
            # - Its left child is balanced (left[0] is True)
            # - Its right child is balanced (right[0] is True)
            # - The difference between left and right height is <= 1
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            
            # Standard height formula you just mastered!
            height = 1 + max(left[1], right[1])
            
            return [balanced, height]
        
        # Run our helper and return just the boolean balance status
        return dfs(root)[0]