class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def primeFactorization(n: int) -> list[int]:
            factorization: list[int] = []
            d = 2

            while d * d <= n:
                while n % d == 0:
                    factorization.append(d)
                    n //= d
                d += 1
            if n > 1:
                factorization.append(n)
            
            return factorization
        res=set()
        for num in nums:
            factor=primeFactorization(num)
            res=res.union(set(factor))
        return len(res)