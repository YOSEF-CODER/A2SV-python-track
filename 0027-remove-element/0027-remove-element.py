class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        output=0
        for x in nums:
            if int(x) == val:
                output+=1
                # nums.remove(val)
        print(output)
        for x in range(output):
            nums.remove(val)
            print(nums)
        # for x in range(output):
        #     nums.append('_')
        print(output)
        return len(nums)