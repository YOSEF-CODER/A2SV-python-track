class Solution:
    def fib(self, n: int) -> int:
        # #another function written to use memoization
        # memo={}
        # def fibonacci(n):
     
            
        #     if n == 1 or n == 0:
        #         return n
        #     if n not in memo:
        #         memo[n] = fibonacci(n-1) + fibonacci(n-2)

        #     return memo[n]
            
        # return fibonacci(n)

        if n<2:
            return n
        arr=[0 for i in range(n+1)]

        arr[0]=0
        arr[1]=1

        for i in range(2,n+1):
            arr[i]=arr[i-1]+arr[i-2]
        
        return arr[-1]