class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res=0
        start=0
        d=defaultdict(int)
        for end in range(len(fruits)):
            d[fruits[end]]+=1
            if len(d)>2:
                if d[fruits[start]]==1:
                    d.pop(fruits[start])
                else:
                    d[fruits[start]]-=1
                start+=1
            res=max(res,end-start+1)  
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        

