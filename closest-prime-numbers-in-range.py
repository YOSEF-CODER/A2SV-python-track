class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        primes=[]


        ans = []

        def isPrime(num: int) -> bool:
            if num < 2:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True


   

        for i in range(left, right + 1):
            if isPrime(i):
                primes.append(i)
                if len(primes) >= 2:

                    if primes[-1] - primes[-2] <= 2:
                        ans = [primes[-2], primes[-1]]
                        break
                   
                    if ans and primes[-1] - primes[-2] < (ans[1] - ans[0]):
                        ans = [primes[-2], primes[-1]]
                    
                    elif not ans:
                        ans = [primes[-2], primes[-1]]
        
       
        if ans:
            return ans
        else:
            return [-1,-1]