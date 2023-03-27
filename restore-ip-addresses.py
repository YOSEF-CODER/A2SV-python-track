class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []

        def backtrack(i, arr):
       
            if len(arr) == 4:
                if i == len(s):
                    string = ".".join(arr)
                    answer.append(string)
                    return
            
            for j in range(i+1, len(s)+1):
                if j-i > 1 and s[i] == "0":
                    break
                if int(s[i:j]) > 255:
                    break
                backtrack(j, arr + [s[i:j]])
            
        backtrack(0, [])
        return answer