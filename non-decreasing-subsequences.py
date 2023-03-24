class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer=[]

        def backtrack(index,arr):
            nonlocal answer

            if index>=len(nums):
                return

            if len(arr)>=1:
                if arr[-1] <= nums[index]:
                    arr.append(nums[index])
                    if arr not in answer:
                        answer.append(arr)
                else:
                    return
            else:
                arr.append(nums[index])


            for j in range(index+1,len(nums)):
                backtrack(j,arr.copy())

        for i in range(len(nums)):
            backtrack(i,[])

        return answer