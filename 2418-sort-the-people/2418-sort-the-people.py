class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
             for j in range(i,len(heights)):
                    if heights[i]<heights[j]:
                        names[j],names[i]=names[i],names[j]
                        heights[j],heights[i]=heights[i],heights[j]
        return names
                    