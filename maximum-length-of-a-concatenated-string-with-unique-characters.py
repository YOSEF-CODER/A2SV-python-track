class Solution:
    def maxLength(self, arr: List[str]) -> int:
        Max=0
        N=len(arr)
        Set=set()
        def backtrack(index,Set):
            nonlocal N,Max

            curSize=len(Set)

            Max=max(Max,curSize)

            for i in range(index,N):
                merged=Set.union(set(arr[i]))

                if len(merged)== curSize + len(arr[i]):
                    backtrack(i+1,merged)
        backtrack(0,Set)
        return Max