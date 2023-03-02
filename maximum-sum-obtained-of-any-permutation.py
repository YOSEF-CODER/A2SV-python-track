class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # Sort the given array
        nums.sort()
        N = len(nums)
        
        # Create a prefix array that represents the frequency of each index in the requests list
        prefix_freq = [0]*(N+1)
        
        # Get the frequency of each index by processing the prefix array
        for start, end in requests:
            prefix_freq[start] += 1
            prefix_freq[end+1] -= 1
        
        # Compute the cumulative sum of the prefix array to get the actual frequencies
        for i in range(1,N):
            prefix_freq[i] += prefix_freq[i-1]
        
        # Remove the offset and sort the prefix array
        prefix_freq.pop()
        prefix_freq.sort()
        
        # Compute the maximum sum by summing up the products of the sorted array and the sorted prefix array
        max_sum = 0
        for i in range(N):
            max_sum += prefix_freq[i]*nums[i]
    
        # Return the maximum sum modulo a certain limit
        return max_sum % (10**9+7)