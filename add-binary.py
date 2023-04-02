class Solution:
    def addBinary(self, a: str, b: str) -> str:
      ans=''
      carry=0
      i=len(a)-1
      j=len(b)-1

      while i>=0 or j>=0 or carry:
        if i>=0:
          carry+=int(a[i])
        else:
          0
        if j>=0:
          carry+=int(b[j])
        else:
          0
        
        ans=str(carry%2)+ans

        carry=carry//2

        i-=1
        j-=1

      return ans