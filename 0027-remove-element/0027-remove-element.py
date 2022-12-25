class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        output=0
        for x in nums:
            if int(x) == val:
                output+=1
        for x in range(output):
            nums.remove(val)
        return len(nums)