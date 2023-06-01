class Solution:
    def rob(self, nums: List[int]) -> int:

        # def dp(i, memo={}):
        #     if i in memo:
        #         return memo[i]
            
        #     if i >= len(nums):
        #         return 0
        #     memo[i] = nums[i]+(max(dp(i+2), dp(i+3)))
        #     return memo[i]
            
        # return dp(0)
        rob1,rob2=0,0
        for n in nums:
            temp=max(rob1+n,rob2)
            rob1=rob2
            rob2=temp

        return rob2