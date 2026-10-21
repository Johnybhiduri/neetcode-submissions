from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n-1:
            return False

        neighbours = defaultdict(list)
        for edge in edges:
            neighbours[edge[0]].append(edge[1])
            neighbours[edge[1]].append(edge[0])
        
        visited = set()
        

        def dfs(node, parent):
            # add node in visited
            visited.add(node)

            for neighbour in neighbours[node]:
                if neighbour == parent:
                    continue
                
                if neighbour in visited:
                    return False
                
                if dfs(neighbour, node) is False:
                    return False
            
            return True

        if dfs(0, -1) is False:
            return False
        
        return len(visited) == n