q = list(map(int,input().split()))
n=q[0]
m=q[1]
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
li=[]
l=0


# print(arr1)
# print(arr2)

for r in range(len(arr2)):
    while l<len(arr1):
        if arr2[r]>arr1[l]:
            l+=1
        else:
           break
    li.append(l)

print(*li)
