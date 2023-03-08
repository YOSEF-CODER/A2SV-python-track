# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper( root, low=float('-inf'),  high=float('inf')):
            if not root:
                return True
            else:
                return helper(root.left,low,root.val) and (low<root.val<high) and helper(root.right,root.val,high)
        return helper(root)