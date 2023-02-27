class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans=0
        res=0
        d=defaultdict(int)
        d[0]=1
        
        for num in nums:
            res+=num
            key=res%k
            if key in d:
                ans+=d[key]
                d[key]+=1
            else:
                d[key]+=1
        return ans