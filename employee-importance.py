"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance=0
        d={}

        for e in employees:
            d[e.id]=e
        
        def dfs(em):
            nonlocal importance

            importance+=d[em].importance

            for e in d[em].subordinates:
                dfs(e)

        dfs(id)
        return importance