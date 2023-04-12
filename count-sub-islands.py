class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
   

        def inbound(row, col):
            return (0 <= row < len(grid1) and 0 <= col < len(grid1[0]))

        def dfs( r, c):

            nonlocal issubset

            if grid1[r][c]!=grid2[r][c]:
                issubset=0
            grid2[r][c]=0 


 

            for row_change, col_change in directions:
                new_row = r + row_change
                new_col = c + col_change
                if inbound(new_row, new_col) and grid2[new_row][new_col]:
                    dfs( new_row, new_col)



        count=0

        for r in range(len(grid1)):
            for c in range(len(grid1[0])):
                
                if grid1[r][c]==grid2[r][c]==1:
                    issubset=1
                    dfs(r,c)
                    count+=issubset

        return count