class Solution:
    def fib(self, n: int) -> int:
        #another function written to use memoization
        memo={}
        def fibonacci(n):
           
            
            if n == 1 or n == 0:
                return n
            if n not in memo:
                memo[n] = fibonacci(n-1) + fibonacci(n-2)

            return memo[n]
            
        return fibonacci(n)