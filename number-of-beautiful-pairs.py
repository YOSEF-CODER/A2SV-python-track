class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            n = nums[i]
            while n > 9:
                n //= 10
            for j in range(i+1, len(nums)):
                x = n
                y = nums[j] % 10
                while y:
                    x, y = y, x % y
                if x == 1:
                    count += 1
        return count