class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        d=defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                d[i-j].append(matrix[i][j])
        for value in d.values():
            res=value.count(value[0])==len(value)
            if not res:
                return False
        return True