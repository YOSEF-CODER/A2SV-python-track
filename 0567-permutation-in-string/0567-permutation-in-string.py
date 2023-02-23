class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length=len(s1)
        left=0
        right=length-1
        s1dict=defaultdict(int)
        s2dict=defaultdict(int)
        ans=False
        if length > len(s2):
            return ans
        for s in s1:
            s1dict[s]+=1
    
        for i in range(length):
            s2dict[s2[i]]+=1
     
        
        if s1dict==s2dict:
            return True
        right+=1
        left+=1
    
        while right<len(s2):
            if s2dict[s2[left-1]]==1:
                s2dict.pop(s2[left-1])
            elif s2dict[s2[left-1]]>1:
                s2dict[s2[left-1]]-=1
            s2dict[s2[right]]+=1
   
            if s1dict==s2dict:
                return True
            right+=1
            left+=1

        return ans

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    