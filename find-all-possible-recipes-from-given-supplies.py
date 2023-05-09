class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        N=len(recipes)
        supplies=set(supplies)
        indegree=defaultdict(int)
        orderdrecipe=[]
        adjlist=defaultdict(list)
        queue=deque()


        for i in range(N):
            for j in range(len(ingredients[i])):
                if ingredients[i][j] not in supplies:
                    adjlist[ingredients[i][j]].append(recipes[i])
                    indegree[recipes[i]]+=1
       

        for i in range(N):
            if indegree[recipes[i]]==0:
                queue.append(recipes[i])

        # print(queue)
        while queue:
            # for _ in range(len(queue)):
            recipe=queue.popleft()
            orderdrecipe.append(recipe)

            for x in adjlist[recipe]:
                indegree[x]-=1
                if indegree[x]==0:
                    queue.append(x)
        return orderdrecipe