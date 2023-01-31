class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        trainers.sort()
        players.sort()
        j=0
        i=0
        count=0
        
        while i < len(players) and j<len(trainers):
            print(players[i],trainers[j])
            if players[i]<=trainers[j]:
                count+=1
                j+=1
                i+=1
                
            else:
                j+=1
             

          
        return count
                
        