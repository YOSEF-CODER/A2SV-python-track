# Enter# Enter your code here. Read input from STDIN. Print output to STDOUT
testcases = int(input())

for i in range(testcases):
    size = int(input())
    b = [int(i) for i in input().split(' ')]
    
    top = b[0] if b[0]>b[-1] else b[-1]
    left, right = 0, size-1
    
    while(left < right):
        if(b[left] >= b[right]):
            if(top >= b[left]):
                top = b[left]
                left+=1
            else:
                print("No")
                break
        
        else:
            if(top >= b[right]):
                top = b[right]
                right-=1
            else:
                print("No")
                break
    if(left == right): 
        print("Yes")
        
