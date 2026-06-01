class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj={i: [] for i in range(numCourses)}
        
        for p,c in prerequisites:
            adj[p].append(c)
        
        visited=set()
        
        def dfs(course):
            if course in visited:
                return False
            if adj[course]==[]:
                return True

            visited.add(course)
            for c in adj[course]:
                if not dfs(c):
                    return False
            visited.remove(course)
            adj[course]=[]
            return True    

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True