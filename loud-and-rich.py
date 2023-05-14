class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        visited = set()
        for x, y in richer:
            graph[y].append(x)
        print(graph)
        
        ans = [-1 for _ in range(len(quiet))]
        d = defaultdict(int)
        

                
        def dfs(mini):

            if ans[mini] == -1: 
                ans[mini] = mini
                for i in graph[mini]:
                    val = dfs(i)
                    if quiet[val] < quiet[ans[mini]]:
                        ans[mini] = val 
               
            return ans[mini]
        
        for k in range(len(quiet)):
            dfs(k)
            
        return ans