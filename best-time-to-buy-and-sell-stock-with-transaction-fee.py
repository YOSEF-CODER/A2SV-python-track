class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # BOTTOM UP
        stay=[-prices[0]]
        buy=[0]

        for i in range(1,len(prices)):
            stay.append(max(stay[-1],buy[-1]-prices[i]))
            buy.append(max(buy[-1],stay[-1]+prices[i]-fee))
        
        return buy[-1]