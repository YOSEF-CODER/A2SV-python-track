class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visit=set()
        for i,j in adjacentPairs:
            graph[i].append(j)
            graph[j].append(i)
        ans = []
        queue=deque()

        for key,lst in graph.items():
            if len(lst)==1:
                if key not in visit:
                    queue.append(key)
                    visit.add(key)
                while queue:
                    node=queue.popleft()
                    ans.append(node)
                    for neigh in graph[node]:
                        if neigh not in visit:
                            queue.append(neigh)
                            visit.add(neigh)
        return ans


 
































        visited = set(ans)
        print(dic)
        while len(ans) <= len(adjacentPairs):
            x = ans[-1]
            for i in dic[x]:
                if i not in visited: 
                    ans.append(i)
                    visited.add(i)
        
        return ans