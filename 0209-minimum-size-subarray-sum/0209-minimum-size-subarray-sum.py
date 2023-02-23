class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        a=float("inf")
        res=float("inf")
        sum=0
        for right in range(len(nums)):
            sum+=nums[right]
            while(sum>=target):
                res=min(res,right-left+1)
                sum-=nums[left]
                left+=1
        return res if res<a else 0
        