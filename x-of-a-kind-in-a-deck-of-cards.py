class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        arr=list(Counter(deck).values())

        if min(arr)<=1:
            return False

        for i in range(1,len(arr)):
            if gcd(arr[i-1],arr[i])<=1:
                return False

        return True