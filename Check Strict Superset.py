# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    super = set(map(int, input().split()))
    N=int(input())
    output=True
    for x in range(N):
        sub=set(map(int, input().split()))
        if not super.issuperset(sub) or len(super) <= len(sub):
            output=False
    print(output)
     
    
