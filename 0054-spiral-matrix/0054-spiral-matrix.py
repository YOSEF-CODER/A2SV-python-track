class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        left,right=0,len(matrix[0])
        top,down=0,len(matrix)
        
        while left<right and top<down:
            #get everything at the top row
            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1
            
            #get every i in the right corner
            for i in range(top,down):
                res.append(matrix[i][right-1])
            right-=1
            
            
            if not (left<right and top<down):
                break
            
            #get everything at the down row
    
            for i in range(right-1,left-1,-1):
                res.append(matrix[down-1][i])
            down-=1
            
            #get every i in the left corner
            for i in range(down-1,top-1,-1):
                res.append(matrix[i][left])
            left+=1
            
        
        
        
        
        return res
        
         
            