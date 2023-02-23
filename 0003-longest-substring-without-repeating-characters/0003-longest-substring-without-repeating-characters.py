class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen=0
        left=0
        for right in range(len(s)):
            firstIndex=s.index(s[right],left)
            if firstIndex!=right:
                left=firstIndex+1
            maxLen=max(maxLen,right-left+1)



        
        return maxLen;