class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start=0
        end=len(nums)-1
        i=0
        
        while i<=end and start<end:
            if nums[i]==0:
                nums[i]=nums[start]
                nums[start]=0
                start+=1
                i+=1
            elif nums[i]==2:
                nums[i]=nums[end]
                nums[end]=2
                end-=1
            else:
                i+=1