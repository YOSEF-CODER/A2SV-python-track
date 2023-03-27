# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.Count=0
        self.Map=defaultdict(int)
        self.Map[0]=1

        def countPath(node,rsum):
            if not node:
                return
            rsum+=node.val
            self.Count+=self.Map[rsum-targetSum]
            self.Map[rsum]+=1

            countPath(node.left,rsum)
            countPath(node.right,rsum)

            self.Map[rsum]-=1


        countPath(root,0)

        return self.Count