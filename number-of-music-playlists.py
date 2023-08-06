from math import factorial
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        if goal == n:
            return factorial(n)% (10**9 + 7)
        
        @cache
        def solve(idx, diff, left):
            if idx >= goal:
                return 0
            if goal - idx == left:
                return factorial(left)
            repeat, new = 0, 0
            if diff >= k:
                repeat = (n-diff) * solve(idx+1, diff, left)
            new = left * solve(idx+1, diff+1, left - 1)
            return new+repeat 
        res = solve(0, 0, n)

        return res % (10**9 + 7)