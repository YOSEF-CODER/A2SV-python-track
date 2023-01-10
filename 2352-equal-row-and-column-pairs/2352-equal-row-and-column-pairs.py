class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count=Counter()
        for i in grid:
            count[tuple(i)]+=1
        
        ans=0
        for i in range(len(grid)):
            
            row1=[]
            for j in range(len(grid)):
                row1.append(grid[j][i])
                ans+=count[tuple(row1)]
        return ans
