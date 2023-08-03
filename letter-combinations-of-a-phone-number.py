class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        phone = {'2':"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        def backtrack(start,substring):
            if len(substring)==len(digits):
                res.append(substring[:])
                return
            
            for i in range(start,len(digits)):
                for letter in phone[digits[i]]:
                    new_str = substring + letter
                    backtrack(i+1,new_str)
        backtrack(0,"")
        return res