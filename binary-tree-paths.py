# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        def pathCount(root,path):
            if not root:
                return
            path=path+str(root.val)+'->'
            if not root.left and not root.right:
                ans.append(path[:-2])
                return
            pathCount(root.left,path)
            pathCount(root.right,path)
        pathCount(root,'')
        return ans