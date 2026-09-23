from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        minutes = 0
        while queue and fresh > 0:
            size = len(queue)

            for i in range(size):
                cell = queue.popleft()

                directions = [(cell[0]-1, cell[1]),
                (cell[0] + 1, cell[1]), 
                (cell[0], cell[1] -1),
                (cell[0], cell[1]+1)]

                for neighbour in directions:
                    if neighbour[0] < 0 or neighbour[1] < 0 or neighbour[0] >= len(grid) or neighbour[1] >= len(grid[0]):
                        continue
                    row = neighbour[0]
                    col = neighbour[1]
                    if grid[row][col] != 1:
                        continue
                    
                    grid[row][col] = 2
                    fresh -= 1
                    queue.append((row,col))

            minutes += 1

        if fresh == 0:
            return minutes
        else:
            return -1

