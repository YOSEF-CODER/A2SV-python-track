class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        if len(piles)==1:
            return math.ceil(piles[0]/h)

        while left<=right:
            mid=(left+right)//2
            hour=0
            for p in piles:
                hour+=math.ceil(p/mid)
            if hour<=h:
                right=mid-1
            else:
                left=mid+1

        return left