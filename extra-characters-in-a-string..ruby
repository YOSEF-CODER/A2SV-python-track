class Solution:
    def logic(self, ind, s, hashDict, dp):

        if ind==len(s):
            return 0
        if ind in dp:
            return dp[ind]
        
        tmp_s=""
        ans=self.logic(ind+1, s, hashDict, dp)+1
        for i in range(ind, len(s)):
            tmp_s+= s[i]
            if tmp_s in hashDict:
                ans=min(ans, self.logic(i+1, s, hashDict, dp))
        dp[ind]=ans
        return ans



    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        hashDict=frozenset(dictionary)
            
        print(hashDict)

        return self.logic(0, s, hashDict, {})