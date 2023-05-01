# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        nodes=[]
        summ=0

        def sumEven(root):
            nonlocal summ
            if not root:
                return

            nodes.append(root.val)

            if len(nodes)>=3 and nodes[-3]%2==0:
                summ+=root.val

            sumEven(root.left)
            sumEven(root.right)
            nodes.pop()

        sumEven(root)

        return summ