class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return searchlist(nums,target)
      
def searchlist(nums,target):
  low,high = 0,len(nums)-1
  while low<=high:
    mid = (low+high)//2
    if nums[mid]==target:
      return mid
    #check if mid in left sorted arr
    if nums[mid]>=nums[low]:
      if target>=nums[low] and target<nums[mid]:
        high = mid - 1
      else:
        low = mid + 1
        
    #check if mid in right sorted arr    
    else:
      if target<=nums[high] and target>nums[mid]:
        low = mid+1
      else:
        high = mid-1
        
  return -1