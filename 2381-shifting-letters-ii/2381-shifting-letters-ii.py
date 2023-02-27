class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N=len(s)
        delta=[0]*(N+1)
        for start,end,direction in shifts:
            if direction==1:
                delta[start]+=1
                delta[end+1]-=1
            else:
                delta[start]-=1
                delta[end+1]+=1 
        for i in range(1,N):
            delta[i]+=delta[i-1]
            
        ans=[]
        orda=ord('a')
        
        for i,c in enumerate(s):
            current=(ord(c)-orda+delta[i])%26
            ans.append(chr(current+orda))
        
        
        
        return ''.join(ans)