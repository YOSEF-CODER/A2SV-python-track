class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans=[]

        def dfs(index,path):
            if index == len(graph)-1:
                return ans.append(path)

            for neighbours in graph[index]:
                dfs(neighbours,path+[neighbours]) 
            
        dfs(0,[0])

        return ans