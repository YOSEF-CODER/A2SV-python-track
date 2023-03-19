# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def traverse(root):
            if not root:
                return []
            return traverse(root.left)+traverse(root.right)+[root.val]

        #    traverse(root.left)
        #    ans.append(root.val)
        #    traverse(root.right)
        ans=traverse(root)
        return ans