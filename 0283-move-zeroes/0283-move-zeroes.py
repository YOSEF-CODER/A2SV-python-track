class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        count=0
        for i in range(n):
            if nums[i] == 0:
                nums.append(0)
                count+=1
        for i in range(count):
            nums.remove(0)
        