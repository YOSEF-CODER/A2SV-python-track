class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
      

        degree=[len(adj) for adj in graph]

        maxRank=0

        for i in range(n):
            for j in range(i+1,n):
                rank=degree[i]+degree[j]
                if j in graph[i]:
                    rank-=1
                maxRank=max(maxRank,rank)
        return maxRank