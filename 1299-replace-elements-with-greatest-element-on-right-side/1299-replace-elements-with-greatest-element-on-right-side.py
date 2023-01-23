class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        if n==1:
            return [-1]
        ans=[]
        greatest=max(arr[1:])
        greatestIndex=arr.index(greatest)
        
        for i in range(n-1):
            if arr[i]==greatest:
                greatest=max(arr[i+1:])
                greatestIndex=arr.index(greatest)
                ans.append(greatest)
            else:
                ans.append(greatest)
        ans.append(-1)
        return ans