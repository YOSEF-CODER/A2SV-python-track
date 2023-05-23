class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        parent = [i for i in range(n)]
        maxx=nums[:]
        ans=[0]
        maximum=0
        allow=set()
 
       
        size = [1]*n
      
        def find(member):
            if member == parent[member]:
                return member
            return find(parent[member])
            
        def union(x,y):

            nonlocal maximum
           
            xpar = find(x)
            ypar = find(y)

            if xpar != ypar:
                if size[xpar] > size[ypar]:
                    parent[ypar] = xpar
                    size[xpar] += size[ypar]
                    maxx[xpar]+=maxx[ypar]
                    maximum=max(maximum,maxx[xpar])
                 
                else:
                    parent[xpar] = ypar
                    size[ypar] += size[xpar]
                    maxx[ypar]+=maxx[xpar]
                    maximum=max(maximum,maxx[ypar])

        for i in range(len(removeQueries)-1,0,-1):
            if removeQueries[i]+1 in allow:
                union(removeQueries[i]+1,removeQueries[i])
            if removeQueries[i]-1 in allow:
                union(removeQueries[i]-1,removeQueries[i])
            allow.add(removeQueries[i])
            maximum=max(maximum,nums[removeQueries[i]])
            ans.append(maximum)
        return reversed(ans)