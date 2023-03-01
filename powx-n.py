class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(base,exp):
            if exp==0:
                return 1
            elif exp % 2 == 0:
                return helper(base*base,exp//2)
            else:
                return base * helper(base*base,(exp-1)//2)
        F=helper(x,abs(n))
        return float(F) if n>=0 else 1/F