class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        ans=set(nums[0].copy())
        
        for i in range(len(nums)):
            nums[i]=set(nums[i])
        
        for i in range(len(nums)):
            ans=ans.intersection(nums[i])

        ans=list(ans)
        ans.sort()
        return ans