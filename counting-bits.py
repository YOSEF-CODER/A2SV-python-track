class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]

        for i in range(n+1):
            bitCount=0
            while i > 0:
                bitCount+=i&1
                i=i>>1
            ans.append(bitCount)
        return ans