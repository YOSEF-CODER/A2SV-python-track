from collections import defaultdict


n=int(input())
k=int(input())

graph=defaultdict(list)

def vertex(v):
    print(*graph[v])

def addEdege(u,v):
    graph[u].append(v)
    graph[v].append(u)

for i in range(k):
    arr=list(map(int,input().split()))

    if arr[0]==1:
        addEdege(arr[1],arr[2])
    elif arr[0]==2:
        vertex(arr[1])
