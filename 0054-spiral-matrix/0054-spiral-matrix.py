class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        element=[]
        while matrix:
        
            #top
         
            element+=matrix.pop(0)
            
       
            #right
            element += [mat.pop() for mat in matrix] 
            
            if not matrix or not matrix[0]: 
                break
             
   
            #bottom
            # if matrix:
            element+=matrix.pop()[::-1]
            
       
            #left            
            element += [mat.pop(0) for mat in matrix][::-1]
            
            if not matrix or not matrix[0]: 
                break
        return element