class Solution:
    def printVertically(self, s: str) -> List[str]:
        max_str_len=0
        words=s.split()
        li=[]
              
        for x in words:
            max_str_len=max(max_str_len,len(x))
            
        
        j=0
        for x in range(max_str_len):
            w=[]
            for i in range(len(words)):
                if j>=len(words[i]):
                    w.append(' ')
                else:
                    w.append(words[i][j])
            w=''.join(w)
            li.append(w.rstrip())
            j=j+1
           
        
        return(li)
        
        
     
      


