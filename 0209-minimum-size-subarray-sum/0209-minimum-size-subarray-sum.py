class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start=0
        end=0
        min_size=float('inf')
        current_sum=0
                
        while end<len(nums):
            current_sum+=nums[end]
            end+=1
            
            while start<end and current_sum>=target:
                current_sum-=nums[start]
                start+=1
                
                min_size=min(min_size,end-start+1)
        
        

        return min_size if min_size<float('inf') else 0
        