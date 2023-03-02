class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        pair=[[pos,speed] for pos,speed in zip(position,speed)]
        pair=sorted(pair)[::-1]
        print(pair)
        for pos , speed in pair:
            stack.append((target-pos)/speed)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)