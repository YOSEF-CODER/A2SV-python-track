class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans=[]



        def backtrack(idx,path):
            ans.append(path[:])

            for i in range(idx,len(nums)):
                backtrack(i+1,path+[nums[i]])

        # backtrack(0,[])

            # if idx>=len(nums):
            #     ans.append(path[:])
            #     return

            # path.append(nums[idx])
            # backtrack(idx+1,path)
            # path.pop()
            # backtrack(idx+1,path)


        backtrack(0,[])
        return ans