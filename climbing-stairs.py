class Solution:
    def climbStairs(self, n: int) -> int:

        def climb(n, memo={}):
            if n in memo:
                return memo[n]
            
            if n < 0:
                return 0
            elif n == 0 or n==1:
                return 1

            memo[n] = climb(n-1,memo) + climb(n-2,memo)
            return memo[n]
            
        return climb(n)