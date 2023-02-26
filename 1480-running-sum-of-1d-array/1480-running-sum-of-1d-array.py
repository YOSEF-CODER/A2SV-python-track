class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix=[0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        prefix.pop(0)
        return prefix