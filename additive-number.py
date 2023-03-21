class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(nums,i):
            
            if len(nums)>2:
                if nums[-2] + nums[-3]!=nums[-1]:
                    return
                else:
                    if i == len(num):
                        return True


            for j in range(i+1,len(num)+1):
                print(nums)
                if j-i>1 and num[i]=='0':
                    continue
                if backtrack(nums+[int(num[i:j])],j):
                        return True
        if backtrack([],0):
            return True
        else:
            return False