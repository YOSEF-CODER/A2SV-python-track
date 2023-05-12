from typing import List

from collections import *
from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        indeg=[0]*n
        graph=defaultdict(list)
        res=[0]*n

        for a,b in edges:
            graph[a].append(b)
            indeg[b-1]+=1
        # print(graph)
        
        queue=deque()
        
        for i in range(n):
            if indeg[i]==0:
                queue.append((i+1,1))
        # print(queue)
        
        while queue:
            node=queue.popleft()
            res[node[0]-1]=node[1]
            for neigh in graph[node[0]]:
                indeg[neigh-1]-=1
                if indeg[neigh-1]==0:
                    queue.append((neigh,node[1]+1))
        return ' '.join(map(str,res))