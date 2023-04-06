class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans=0

        maxOr=0

        for num in nums:
            maxOr |= num

        def backtrack(idx,curOr):
            nonlocal ans
            if idx == len(nums):
                if curOr==maxOr:
                    ans+=1
                return
            backtrack(idx+1,curOr)
            backtrack(idx+1,curOr | nums[idx])

        backtrack(0,0)
        return ans

        








        return ans