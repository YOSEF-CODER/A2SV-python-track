#User function Template for python3
from collections import *

class Solution:
    def findOrder(self,alien_dict, N, K):
        # print(alien_dict)
        graph=defaultdict(list)
        indeg=defaultdict(int)
        ord=[]
        
        for i in range(N-1):
            word1=alien_dict[i]
            word2=alien_dict[i+1]
            
            for j in range(min(len(word1),len(word2))):
                if word1[j]!=word2[j]:
                    graph[word1[j]].append(word2[j])
                    indeg[word2[j]]+=1
                    break
        
        queue=deque()
        
        for i in range(k):
            if indeg[chr(i+97)]==0:
                queue.append(chr(i+97))
                
        while queue:
            node=queue.popleft()
            ord.append(node)
            
            for neigh in graph[node]:
                indeg[neigh]-=1
                if indeg[neigh]==0:
                    queue.append(neigh)
        # print(ord)
        return "".join(ord)