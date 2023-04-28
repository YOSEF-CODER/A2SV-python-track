class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        direction=[(-1,0),(1,0),(-1,1),(0,-1),(0,1),(1,1),(-1,-1),(1,-1)]

        queue=deque([(0,0)])
        visited=set([(0,0)])
        distance=1
        n=len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1]==1:
            return -1   
       

        while queue:
            l =len(queue)
            for i in range(l):

                node=queue.popleft()
                if node==(n-1,n-1):
                    return distance        
                

                
                for dir in direction:
                
                    x=node[0]+dir[0]
                    y=node[1]+dir[1]

                    if 0 <= x < n and 0 <= y <n:
                        if grid[x][y]==0 and (x,y) not in visited:
                            visited.add((x,y))
                            queue.append((x,y))
            distance+=1
                       

         
        return -1