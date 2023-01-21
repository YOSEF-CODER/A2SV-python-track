class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        res=[[0 for _ in range(n-2)] for _ in range(n-2)]
        
        for i in range(n-2):
            for j in range(n-2):
                best=grid[i][j]
                for ii in range(i,i+3):
                    for jj in range(j,j+3):
                        best=max(best,grid[ii][jj])       
                res[i][j]=best
        
        return res