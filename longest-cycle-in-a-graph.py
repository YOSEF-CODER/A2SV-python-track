class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        n=len(edges)
        visited=set()
        indeg=[0]*n
        q=deque()
        graph=defaultdict(list)

        for idx, el in enumerate(edges):
            if el >= 0:
                graph[idx].append(el)
                indeg[el] += 1

        for i in range(n):
            if not indeg[i]:
                q.append(i)
        print(q)
        while q:
            cur = q.popleft()
            for nbr in graph[cur]:
                indeg[nbr] -= 1
                if not indeg[nbr]:
                    q.append(nbr)
        print(indeg)
        leng = -1
        for i in range(n):
            if indeg[i]:
                q.append(i)
                visited.add(i)
                count = 0

                while q:
                    cur = q.popleft()
                    count += 1
                    if graph[cur][0] in visited:
                        break
                    print(count)
                    for nbr in graph[cur]:
                        q.append(nbr)
                        visited.add(nbr)
                    
                leng = max(leng, count)

        return leng