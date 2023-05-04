class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordrevcounter=defaultdict(int)


        for word in words:
            wordrevcounter[word]-=1

        
        heap=[]

        for word,reverseCount in wordrevcounter.items():
            heap.append((reverseCount,word))

        heapify(heap)

        ans=[]

        for _ in range(k):
            ans.append(heappop(heap)[1])

        return ans