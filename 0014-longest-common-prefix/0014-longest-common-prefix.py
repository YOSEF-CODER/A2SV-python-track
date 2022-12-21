class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      
        size = len(strs)
  
        if size == 0:
            return ""

        if size == 1:
            return strs[0]
        
        s = 300
        for i in range(size):
            s = min(s, len(strs[i]))
        
        if s == 0:
            return ''
        
        
        
        for i in range(s):
            ch = strs[0][i]
            for l in strs:
                if l[i] != ch:
                    return strs[0][:i]
        return strs[0][:i+1]