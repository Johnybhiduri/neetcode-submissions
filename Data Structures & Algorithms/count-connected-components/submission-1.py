from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbours = defaultdict(list)
        for edge in edges:
            neighbours[edge[0]].append(edge[1])
            neighbours[edge[1]].append(edge[0])
        
        count = 0
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbour in neighbours[node]:
                if neighbour not  in visited:
                    dfs(neighbour)
            

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count