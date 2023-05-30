class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        def dp(x):
            tt=float('inf')
            if x ==0:
                return 0
            if x < 0:
                return float('inf')
            if x in memo:
                return memo[x]
            for i in range(len(coins)):
                tt=min(tt,dp(x-coins[i]))
            memo[x]=tt+1
            return memo[x]
        val=dp(amount)
        return val if val != float('inf') else -1