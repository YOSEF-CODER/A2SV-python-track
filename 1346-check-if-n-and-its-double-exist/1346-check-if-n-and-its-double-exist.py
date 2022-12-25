class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        left=0
        right=len(arr)-1
        arr=sorted(arr)
        while left<right:
            if arr[left] * 2 == arr[right] or arr[left] == arr[right] * 2:
                return True
            else:
                if left == right-1:
                    left=0
                    right-=1
                else:
                    left+=1
                    
        return False