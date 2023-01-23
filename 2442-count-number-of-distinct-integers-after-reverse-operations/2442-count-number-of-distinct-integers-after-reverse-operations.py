class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        for i in range(len(nums)):
            if nums[i]==1:
                nums.append(nums[i])
            else:
                sortt=nums[i][::-1]
                nums.append(sortt)     
            
        for i in range(len(nums)):
            nums[i]=int(nums[i])
         
        arr=dict(Counter(nums))
        
        return len(arr)