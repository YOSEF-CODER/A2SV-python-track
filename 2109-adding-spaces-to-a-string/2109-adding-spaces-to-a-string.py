class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
   
        string = []
        
       
        left = 0
        
       
        for right in range(len(spaces)):
            string.append(s[left:spaces[right]]+' ')
            left = spaces[right]
        
        print(string)
        string.append(s[left: len(s)])
        
      
        return ''.join(string)