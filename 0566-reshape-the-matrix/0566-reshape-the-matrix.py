class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
       
      
        size=len(mat)*len(mat[0])
        ans_size=c*r
        
        if ans_size != size:
            return mat
        
        ans=[[0 for i in range(c)] for i in range(r)]
     
        for i in range(size):
            mat_row = i // len(mat[0])
            mat_col = i % len(mat[0])
            ans_row = i // c
            ans_col = i % c
            ans[ans_row][ans_col] = mat[mat_row][mat_col]

        return ans
                    