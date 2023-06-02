class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo={}
        def dp(r,c):
            if r==len(triangle)-1:
                return triangle[r][c]
            if (r,c) in memo:
                return memo[(r,c)]
            memo[(r,c)]=triangle[r][c]+min(dp(r+1,c),dp(r+1,c+1))
            return memo[(r,c)]
        return dp(0,0)