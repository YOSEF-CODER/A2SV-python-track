class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        li=[]
        n=len(boxes)
        index=0
        
        for i in range(n):
            sum=0
            for j in range(n):
                if j!=i:
                   
                    if boxes[j]=='1':
                        x=abs(j-i)
                        sum+=x
            li.append(sum)
        return li