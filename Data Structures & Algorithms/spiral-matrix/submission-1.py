class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1

        left = 0
        right = len(matrix[0]) - 1

        result = []

        while top <= bottom and left <= right:
            # Read Top
            result.extend(matrix[top][left:right+1])
            top+=1

            if top > bottom:
                break


            # Read Right
            for row in range(top, bottom+1):
                result.append(matrix[row][right])
            
            right-=1

            if left > right:
                break

            # Read Bottom
            for col in range(right, left-1, -1):
                result.append(matrix[bottom][col])

            bottom -= 1

            # Read Left
            for row in range(bottom, top-1, -1):
                result.append(matrix[row][left])
                
            left += 1
        
        return result