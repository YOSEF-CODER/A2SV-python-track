class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)

        while left<=right:
            mid=(left+right)//2
            day=1
            summ=0
            for w in weights:
                if summ+w<=mid:
                    summ+=w
                else:
                    day+=1
                    summ=w
            if day<=days:
                right=mid-1
            elif day>days:
                left=mid+1
        return left