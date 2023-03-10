# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        ans=[]
        def traverse(root):
            if not root:
                return []
            return traverse(root.left) + [root.val] + traverse(root.right)

        arr=traverse(root)
        count=Counter(arr)
        v=max(count.values())

        for key in count:
            if count[key]==v:
                ans.append(key)
        return ans