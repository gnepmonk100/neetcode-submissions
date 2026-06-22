# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def findGoodNode(node, maxVal):
            res = 0
            if not node:
                return 0
            if node.val >= maxVal:
                res = 1
            else:
                res = 0
            maxVal = max(node.val, maxVal)
            res += findGoodNode(node.left, maxVal)
            res += findGoodNode(node.right, maxVal)

            return res
        return findGoodNode(root, root.val)
        


        
        