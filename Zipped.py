# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__=="__main__":
    N_items=int(input())
    
    od = OrderedDict()
    
    for _ in range(N_items):
         record =input().split()
              
         price=int(record[len(record)-1])
         record.pop();
         record=" ".join(record)
         od[record]=od.get(record,0)+price
         
for key,value in od.items():
    print(key,value)
