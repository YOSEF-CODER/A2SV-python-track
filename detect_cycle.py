from typing import List
from collections import *
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		color=[-1]*V
		queue=deque()
		def bfs():
		    while queue:
		        node=queue.popleft()
		        color[node]=1
		        for neigh in adj[node]:
		            if color[neigh]==0:
		                return False
		            elif color[neigh]==-1:
		                queue.append(neigh)
		                color[neigh]=0
		    return True
		    
		
		for i in range(V):
		    if color[i]==-1:
		        queue.append(i)
		        color[i]=0
		        if not bfs():
		            return 1
		return 0
		        