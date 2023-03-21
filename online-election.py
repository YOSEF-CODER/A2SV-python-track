class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.votes=defaultdict(int)
        self.times=times

        self.leadings=[]
        n=len(persons)
        cur_max_vote=0

        for i in range(n):
            p=persons[i]
            t=times[i]
            self.votes[p]+=1

            if not self.leadings:
                self.leadings.append(p)
                cur_max_vote=1

            elif self.votes[p] >= cur_max_vote:
                self.leadings.append(p)
                cur_max_vote=self.votes[p]

            else:
                self.leadings.append(self.leadings[-1])

        

    def q(self, t: int) -> int:
        index=bisect_right(self.times,t)-1
        return self.leadings[index]

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)