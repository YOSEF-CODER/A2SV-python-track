class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set([0])
        queue=deque([0])
        length=len(rooms)-1

        
        while queue:
            curRoom = queue.popleft()
            for index in rooms[curRoom]:
                if index not in visited:
                    visited.add(index)
                    queue.append(index)
                    length-=1

        if length == 0:
            return True
        return False