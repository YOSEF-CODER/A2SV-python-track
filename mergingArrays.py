q = list(map(int,input().split()))
n=q[0]
m=q[1]
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
li=[]
l=0
r=0

while l < len(arr1) and r<len(arr2):
    if arr1[l] < arr2[r]:
        li.append(arr1[l])
        l+=1
    elif arr2[r] < arr1[l]:
        li.append(arr2[r])
        r+=1
    elif  arr2[r] == arr1[l]:
        li.append(arr1[l])
        li.append(arr2[r])
        l+=1
        r += 1

while l<len(arr1):
    li.append(arr1[l])
    l += 1
while r<len(arr2):
    li.append(arr2[r])
    r += 1

for i in li:
    print(i,end=' ')
