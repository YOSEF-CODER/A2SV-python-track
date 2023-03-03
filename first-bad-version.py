# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right=1,n
        while left<=right:
            mid=(left+right)//2
            if not isBadVersion(mid):
                left=mid+1
            elif isBadVersion(mid):
                right=mid
            if left==right:
                return right
        return 1