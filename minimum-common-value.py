class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ans=-1

        i=j=0

        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                ans=nums1[i]
                break

        return ans