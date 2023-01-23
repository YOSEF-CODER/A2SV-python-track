class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        
        if len(arr)<3:
            return False
        else:
            tip=max(arr)
            tipIndex=arr.index(tip)
            if(tipIndex==0 or tipIndex==len(arr)-1):
                return False
            
                              
            for i in range(tipIndex):
                if arr[i]>=arr[i+1]:
                    return False
                                            
            for i in range(tipIndex,len(arr)-1):
                if arr[i]<=arr[i+1]:
                    return False
            return True       
                   
        
        
        
        

        