class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_i = []
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odd_i.append(i)
        start = 0
        end = k - 1
        i = 0
        count = 0
        while end < len(odd_i):
            if end == len(odd_i) - 1:
                j = len(nums) - 1
            else:
                j = odd_i[end + 1] - 1
            count = count + (odd_i[start] - i + 1) * (j - odd_i[end] + 1)
            i = odd_i[start] + 1
            start = start + 1
            end = end + 1
        return count