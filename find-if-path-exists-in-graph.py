class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList=defaultdict(list)

        for i,j in edges:
            adjList[i].append(j)
            adjList[j].append(i)

        def findPath(node,visited):
            nonlocal destination

            if node==destination:
                return True

            if node in visited:
                return False

            visited[node]=True

            for path in adjList[node]:
                if findPath(path,visited):
                    return True

        return findPath(source,{})