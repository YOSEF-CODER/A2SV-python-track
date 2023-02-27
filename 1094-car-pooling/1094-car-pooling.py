class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        m=max([e for _,_,e in trips])
        
        lookup=[0]*(m+2)
        for people,st,end in trips:
            lookup[st+1]+=people
            lookup[end+1]-=people
        print(lookup)
        prefix=[0]
        
        for i in range(1,len(lookup)):
            prefix.append(prefix[-1]+lookup[i])
        return max(prefix)<=capacity
            
