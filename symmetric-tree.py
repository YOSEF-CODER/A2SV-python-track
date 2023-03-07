# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p=root.left
        q=root.right
        def helper(p,q):
            if p and not q:
                return False
            if not p and q:
                return False
            if not p and not q:
                return True
            if p.val!=q.val:
                return False
            else:
                return helper(p.left,q.right) and helper(p.right,q.left)
        return helper(p,q)