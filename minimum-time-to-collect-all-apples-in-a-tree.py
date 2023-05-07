class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
      
        adj_list = defaultdict(list)
        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

    
        visited = set()

      
        def dfs(node=0):
            visited.add(node)
            
         
            if len(adj_list[node]) == 1 and node:
                return (2, hasApple[node])
            
         
            current_time = 0
            for child in adj_list[node]:
                if child not in visited:
                    steps, has_sub_apple = dfs(child)
                    if has_sub_apple:
                        current_time += steps
                        

            return (current_time + 2, current_time or hasApple[node])

  
        return dfs()[0] - 2