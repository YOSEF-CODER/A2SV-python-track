class DataStream:

    def __init__(self, value: int, k: int):
        self.q=deque()
        self.val=value
        self.k=k
        self.m=Counter()

    def consec(self, num: int) -> bool:
        self.q.append(num)
        if num==self.val:
            self.m[num]+=1
        while len(self.q)>self.k:
            x=self.q.popleft()
            self.m[x]-=1
            if self.m[x]==0:
                del self.m[x]
        return self.m[self.val]==self.k



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)