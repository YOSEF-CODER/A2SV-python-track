# Templates for the inputs:
from typing import List
from collections import Counter, defaultdict
import sys

def stringInput() -> str:
    return sys.stdin.readline()
    
def listInput() -> List[int]:
    return list(map(int, input().split()))
    
def string_list() -> List[int]:
    return list(input())
def intInput() -> int:
    return int(input())
    

    
def solve():
    # Write your code here...
    prog, math = listInput()
    
    max_possible = (prog + math) // 4
    min_ = min(prog, math)
    
    print(min(min_, max_possible))
    
   
    
# Driver code...    
if __name__ == '__main__':
    for tt in range(intInput()):
        solve()
    
        
        
        
        
        
        
        
    
    
        
    
    
    
        
        
