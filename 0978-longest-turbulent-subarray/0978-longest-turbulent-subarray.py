class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        greater=1
        smaller=1
        n=len(arr)
        ans=1
        
        for i in range(1,n):
            smaller1=greater1=1
            
            if arr[i]>arr[i-1]:
                greater1=smaller+1
            elif arr[i]<arr[i-1]:
                smaller1=greater+1
            ans=max(ans,greater1,smaller1)
            greater=greater1
            smaller=smaller1
            
        return ans