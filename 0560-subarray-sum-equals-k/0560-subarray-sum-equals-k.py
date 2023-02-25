class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        

        n_subarrays=0
        curSum=0
        prefixSums={0:1}
        
        for n in nums:
            curSum+=n
            diff=curSum-k
            
            n_subarrays+=prefixSums.get(diff,0)
            prefixSums[curSum]=1+prefixSums.get(curSum,0)
        
       
        return n_subarrays