class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        N=len(nums)
        def partition(left,right):
            pivot=nums[right]

            i=left-1

            for j in range(left,right):
                if nums[j] <= pivot:
                    i=i+1
                    nums[i],nums[j]=nums[j],nums[i]

            nums[i+1],nums[right]=nums[right],nums[i+1]
            # print(nums)
            return i+1
        
        def quicksort(left,right):


            if right < left:
                return nums[N-k]

            pi=partition(left,right)

            if pi == N-k:
                return nums[pi]
            elif pi < N-k:
                return quicksort(pi+1,right)
            else:
                return quicksort(left,pi-1)
        return quicksort(0,N-1)



        

        return nums[-ans]