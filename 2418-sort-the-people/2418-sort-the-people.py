class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Using bubble sort
        # for i in range(len(heights)):
        #      for j in range(len(heights)-1):
        #             if heights[j]<heights[j+1]:
        #                 names[j],names[j+1]=names[j+1],names[j]
        #                 heights[j],heights[j+1]=heights[j+1],heights[j]
       
        # Using Selection sort sort
        size=len(heights)
        for i in range(size):
            maximum=i
            for j in range(i,size):
                if heights[j]>heights[maximum]:
                    heights[maximum],heights[j]=heights[j],heights[maximum]
                    names[i],names[j]=names[j],names[i]

        return names
                    