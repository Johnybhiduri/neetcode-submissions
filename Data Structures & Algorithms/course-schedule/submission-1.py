class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i  in range(numCourses):
            graph[i] = []
        
        for course in prerequisites:
            c1 = course[0]
            c2 = course[1]
            graph[c2].append(c1)
            
        
        visited = set() #courses we have completely checked
        path = set() #courses currently inside this DFS chain

        def dfs(course):
            if course in path:
                return False
            
            if course in visited:
                return True
            
            path.add(course)

            for nxt_course in graph[course]:
                if dfs(nxt_course) == False:
                    return False
            
            path.remove(course)
            visited.add(course)
        
            return True
        
        for i in range(numCourses):
            if dfs(i) is False:
                return False
        
        return True

