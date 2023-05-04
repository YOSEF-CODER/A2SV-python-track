class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=(-stones[i])

        heapify(stones)

        while len(stones)>1:
            stone1=heappop(stones)
            stone2=heappop(stones)

            if stone1 != stone2:
                heappush(stones, stone1-stone2)

        if stones:
            return -stones[0]

        return 0