    from collections import defaultdict

    n=int(input())
    arr=[]
    graph=defaultdict(list)
    edges=0


    for _ in range(n):
        arr.append(list(map(int,input().split())))
    for i in range(n):
        for j in range(n):
            if arr[i][j] >=1:
                graph[i+1].append(j+1)

    for key, value in graph.items():
        edges+=len(value)
    print(edges//2)
