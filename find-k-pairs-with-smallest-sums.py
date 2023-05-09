class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap=[]

        for n in nums1:
            for m in nums2:
                if len(heap)<k:
                    heappush(heap,(-(n+m),n,m))
                elif heap[0] < (-(n+m),n,m):
                    heapreplace(heap,(-(n+m),n,m))
                else:
                    break
        return [(n,m) for s,n,m in heap]