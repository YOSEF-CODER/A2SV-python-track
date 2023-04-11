class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        adjList=defaultdict(list)

        for i,j in dislikes:
            adjList[i].append(j)
            adjList[j].append(i)
        print(adjList)

        color=defaultdict(int)

        def dfs(node,curr):

            if node in color:
                return color[node]==curr
            color[node]=curr           


            for neighbour in adjList[node]:
                found=dfs(neighbour,1-curr)
                if not found:
                    return False
            return True


            

        for key in adjList:
            if key not in color:
                res=dfs(key,1)
                if not res:
                    return False
        return True