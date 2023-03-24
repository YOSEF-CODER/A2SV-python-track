class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        temp=0

        while i < n:

            cp=nums[i]

            if cp != i:

                if cp==len(nums):
                    temp=cp
                    i+=1
                else:
                    nums[i],nums[cp]=nums[cp],nums[i]

            else:
                i+=1


        if temp==0:
            return len(nums)

        else:
            return nums.index(temp)