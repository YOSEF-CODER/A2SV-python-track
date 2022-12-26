class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=int(len(nums))
        a=(n*(n+1))/2
        b=sum(nums)
        return int(a-b)
   