class Solution:
    def average(self, salary: List[int]) -> float:
        salary=sorted(salary)
        print(salary)
        sum=0
        for i in range(1,len(salary)-1):
            sum+=float(salary[i])
        return sum/(len(salary)-2)