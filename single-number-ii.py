class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # ones=0
        # twos=0
        # for i in nums:
        #     ones=(ones ^ i) & (~twos)
        #     twos=(twos ^ i) & (~ones)
        # return ones

        ans=0

        for pos in range(32):
            count=0
            for num in nums:
                if ((num+(2**31)) & (1<<pos))!=0:
                    count+=1
            ans+=((2**pos)*(count%3))


        return ans-(2**31)