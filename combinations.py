class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def backtrack(index,arr):
            nonlocal ans
            if index > n:
                return
            if len(arr)==k:
                ans.append(arr)
                return
            for i in range(index+1,n+1):
                backtrack(i,arr+[i])

        backtrack(0,[])
        return ans