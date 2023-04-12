# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=[]

        def backtrack(root,num):
            num.append(str(root.val))

            if not root.left and not root.right:
                ans.append(int("".join(num)))

            if root.left:
                backtrack(root.left,num)

            if root.right:
                backtrack(root.right,num)

            num.pop()

        backtrack(root,[])
        return sum(ans)