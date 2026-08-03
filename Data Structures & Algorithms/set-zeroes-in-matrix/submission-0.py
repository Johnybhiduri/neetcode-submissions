class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = {}
        columns = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]== 0:
                    rows[i] = True
                    columns[j] = True
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows:
                    matrix[i][j] = 0
                elif j in columns:
                    matrix[i][j] = 0
