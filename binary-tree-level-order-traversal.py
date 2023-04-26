# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # map=defaultdict(list)
        if not root:
            return []

        # def traverse(root,level):

        #     map[level].append(root.val)

        #     if root.left:
        #         traverse(root.left,level+1)
        #     if root.right:
        #         traverse(root.right,level+1)

        # traverse(root,0)
        # return (list(map.values()))

        queue=deque([root])
        ans=[]
        acc=[root.val]

        while queue:
            ans.append(acc)
            acc=[]

            for i in range(len(queue)):

                node=queue.popleft()

                if node.left:
                    queue.append(node.left)
                    acc.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    acc.append(node.right.val)

        return ans