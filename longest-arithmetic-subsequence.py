class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # Initialize the dynamic programming table
        dp = {}
        n = len(nums)
        max_length = 2
        
        # Iterate over each element in nums
        for i in range(n):
            # Initialize the dp table for the current element
            dp[i] = {}
            
            # Iterate over previous elements
            for j in range(i):
                # Calculate the difference between the current element and previous element
                diff = nums[i] - nums[j]
                
                # Check if the difference exists in the dp table for the previous element
                if diff in dp[j]:
                    # If the difference exists, update the dp table for the current element
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    # If the difference doesn't exist, initialize the dp table for the current element with a length of 2
                    dp[i][diff] = 2
                
                # Update the maximum length
                max_length = max(max_length, dp[i][diff])
        
        return max_length