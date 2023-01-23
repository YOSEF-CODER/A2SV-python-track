q = list(map(int,input().split()))
n=q[0]
k=q[1]
arr=[]
li=[]
ans=[]
for i in range(n):
    arr.append(input())

li=list(zip(*arr))

for i in range(n):
    for j in range(k):
        if arr[i][j] in (arr[i][:j]+arr[i][j+1:]) or arr[i][j] in (li[j][:i]+li[j][i+1:]):
            continue
        else:
            ans.append(arr[i][j])
a=''.join(ans)
print(a)
