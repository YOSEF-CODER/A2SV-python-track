n=int(input())

arr=[]

for i in range(n):
    arr.append(list(map(int,input().split())))

sink=[]
source=[]

for i in range(n):
    if sum(arr[i]) == 0:
        sink.append(i+1)

for col in range(n):
    colsum=0
    for row in range(n):
        colsum+=arr[row][col]
    if colsum==0:
        source.append(col+1)

print(len(source),*source)
print(len(sink),*sink)


