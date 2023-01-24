class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l=0
        r=len(skill)-1
        check=skill[l]+skill[r]
        sum=0
          
        while l<r:
            if check!=skill[l]+skill[r]:
                return -1
            else:
                sum+=skill[l]*skill[r]
                l+=1
                r-=1
        return sum