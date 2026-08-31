class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()

        def dfs(row, col, index):
            if index == len(word):
                return True
            
            # if position outside board
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False

            if (row,col) in visited:
                return False
            
            if board[row][col] !=  word[index]:
                return False
            

            visited.add((row,col))

            # UP - Down - Left - Right
            if dfs(row-1, col, index+1) or dfs(row+1, col,index+1) or dfs(row, col-1, index+1) or dfs(row, col + 1,index+1):  
                visited.remove((row,col)) 
                return True

            visited.remove((row,col))

            return False




        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    if dfs(i, j,0):
                        return True
                    
        
        return False
