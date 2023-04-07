class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans=[]
        reached=[0]*n

        for fri,toi in edges:
            reached[toi]+=1
        for i in range(len(reached)):
            if reached[i]==0:
                ans.append(i)

        return ans