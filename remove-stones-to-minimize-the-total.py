class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles=[-pile for pile in piles]
        heapify(piles)

        for _ in range(k):
            value=heappop(piles)
            print(value)
            value+=(-value//2)
            print(value)
            heappush(piles,value)

        return -sum(piles)