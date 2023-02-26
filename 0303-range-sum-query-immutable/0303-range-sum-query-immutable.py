class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        
    def sumRange(self, left: int, right: int) -> int:
        prefix=[0]
        for i in range(left,right):
            prefix.append(prefix[-1]+self.nums[i])
              
        prefix.append(prefix[-1]+self.nums[right])
        return prefix[-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)