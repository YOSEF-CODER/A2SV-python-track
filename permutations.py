class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []  

        def backtrack(bitTrack, arr):
          
            if len(arr) == len(nums):
                ans.append(arr)  
                return

            for i in range(len(nums)):
                if not (bitTrack & (1 << i)): 
                    bitTrack |= (1 << i) 
                    backtrack(bitTrack, arr + [nums[i]])  
                    bitTrack &= ~(1 << i)  

        backtrack(0, [])
        return ans