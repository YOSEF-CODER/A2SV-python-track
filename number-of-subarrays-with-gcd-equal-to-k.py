class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        res=0

        for i in range(len(nums)):
            curgcd=nums[i]
            if curgcd==k:
                res+=1
            for j in range(i+1,len(nums)):
                curgcd=gcd(curgcd,nums[j])
                if curgcd==k:
                    res+=1

        return res