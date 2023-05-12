class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        result=[]
        in_degree=[0]*numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            in_degree[a]+=1

         # Initialize the queue with nodes having no incoming edges
        queue = deque([node for node in graph if in_degree[node] == 0])


        while queue:
            node=queue.popleft()
            result.append(node)

            for i in graph[node]:
                in_degree[i]-=1
                if in_degree[i]==0:
                    queue.append(i)

        for dep in in_degree:
            if dep:
                return False
        return True