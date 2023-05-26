class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        def MinCost(n, memo={}):
            nonlocal N
            
            if n >= N:
                
                return 0
            
            if n in memo:
                return memo[n]

            memo[n] = cost[n] + min(MinCost(n+1,memo), MinCost(n+2,memo))
            return memo[n]
            
        return min(MinCost(0), MinCost(1))