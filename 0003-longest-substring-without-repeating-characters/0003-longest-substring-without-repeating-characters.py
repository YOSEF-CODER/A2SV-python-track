class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength=0
        left=0
        
        for right in range(len(s)):
            firstApperanceIndex=s.index(s[right],left)
        
            if firstApperanceIndex!=right:
                
                left=firstApperanceIndex+1
                
            
            maxLength=max(maxLength,right-left+1)

        
        return maxLength;