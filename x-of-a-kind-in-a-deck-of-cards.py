class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck)==1:
            return False

        arr=list(Counter(deck).values())

        partition=gcd(*arr)

        if partition == 1:
            return False




        return True