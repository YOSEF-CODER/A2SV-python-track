class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        output=[-1]*len(nums)

        for i in range(len(nums)):
            while stack and nums[i]>nums[stack[-1]]:
                output[stack.pop()]=nums[i]
            stack.append(i)
        for i in range(len(nums)):
            while stack and nums[i]>nums[stack[-1]]:
                output[stack.pop()]=nums[i]
            if not stack:
                break
        return output