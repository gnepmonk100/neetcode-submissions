# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while curr:
            # If both target nodes are greater than current, go right
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both target nodes are less than current, go left
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # We found the split point (or found one of the nodes itself)
            else:
                return curr