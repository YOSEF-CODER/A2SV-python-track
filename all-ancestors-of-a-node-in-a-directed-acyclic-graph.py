class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegree=[0]*n
        adjlist=defaultdict(list)
        ans=[set() for i in range(n)]

        for e in edges:
            adjlist[e[0]].append(e[1])
            indegree[e[1]]+=1

        queue=deque()


        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
        # print(indegree)
        # print(queue)
        # print(adjlist)
        while queue:
            x=queue.popleft()
            for nums in adjlist[x]:
                ans[nums].add(x)
                for i in ans[x]:
                    ans[nums].add(i)
                indegree[nums]-=1
                if indegree[nums]==0:
                    queue.append(nums)
        ans=[sorted(list(i)) for i in ans]
        return ans