class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:        
        for i in range(len(matrix) - 1):
            for j in range(i+1, len(matrix)):
               matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # reverse the array
        for i in range(len(matrix)):
            matrix[i].reverse()
        
        

