class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m
        j = 0
        for i in range(len(nums1)-m):
            nums1[m] = nums2[j]
            j = j +1
            m = m+1
            if j > n: break
         
        nums1.sort()
        print(nums1)
        