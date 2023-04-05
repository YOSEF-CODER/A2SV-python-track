class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans=[]



        def backtrack(idx,mask):
            subset=[]

            for i in range(len(nums)):
                if mask&(1<<i):
                    subset.append(nums[i])

            ans.append(subset[:])

            for i in range(idx,len(nums)):
                mask |= (1<<i)
                backtrack(i+1,mask)
                mask &= ~(1<<i)



        backtrack(0,0)
        return ans