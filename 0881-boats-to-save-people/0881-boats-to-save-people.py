class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i=0
        j=len(people)-1
        num_boats=0
        people.sort()
        
        while i<=j:
            if people[i]+people[j]<=limit:
                i+=1
                j-=1
            else:
                j-=1
            num_boats+=1
        return num_boats