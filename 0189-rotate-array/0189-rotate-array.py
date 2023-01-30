class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k==0:
            return 
        elif k==len(nums):
            return 
        elif len(nums)==1:
            return 
        elif len(nums)==2:
            nums.reverse()
            return 
        else:
            nums.reverse()
            l=k%len(nums)
            r=len(nums)-1

            while l<=r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
            l=0
            r=k%len(nums)-1
            while l<=r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        
