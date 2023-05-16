class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        result = [set() for _ in range(n)]
        indeg = [0] * (n)
        graph = defaultdict(list)
        q = deque()

        for a, b in prerequisites:
            graph[a].append(b)
            indeg[b] += 1

        q = deque([node for node in graph if indeg[node] == 0])
        while q:
            node = q.popleft()
            for nbr in graph[node]:
                result[nbr].add(node)
                for el in result[node]:
                    result[nbr].add(el)
                indeg[nbr] -= 1
                if not indeg[nbr]:
                    q.append(nbr)

        
        ans = []
        for u, v in queries:
            ans.append(u in result[v])

        return ans