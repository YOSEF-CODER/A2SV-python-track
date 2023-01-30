class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=0
        c=Counter(nums)
        seen=set()
        for x in c:
            if x not in seen and (k-x) in c:
                if x == k-x:
                    count+=c[x]//2
                else:
                    count+=min(c[x],c[k-x])
                seen.add(x)
                seen.add(k-x)
        return count