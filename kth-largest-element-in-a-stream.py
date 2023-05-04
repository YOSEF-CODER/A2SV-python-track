class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=nums
        self.k=k
        self.heap=[]
        for num in self.nums:
            heappush(self.heap,num)
            if len(self.heap) > self.k:
                heappop(self.heap)
     
        

    def add(self, val: int) -> int:
        heappush(self.heap,val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]

        

        
            


      
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)