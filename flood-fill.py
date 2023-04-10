class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row=len(image)
        col=len(image[0])

        original=image[sr][sc]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visited=set()

        def flood(i,j):
            if not(0<=i<row) or not(0<=j<col):
                return
            if image[i][j] != original or (i,j) in  visited:
                visited.add((i,j))
                return
               
            else:
                image[i][j]=color
                visited.add((i,j))

            
            for dir in directions:
                flood(i+dir[0],j+dir[1])

        flood(sr,sc)

        return image