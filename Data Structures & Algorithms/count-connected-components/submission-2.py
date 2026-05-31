class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj=[[] for _ in range(n)]
        visited=[False]*n

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(n):
            visited[n]=True
            for neighbor in adj[n]:
                if not visited[neighbor]:
                    dfs(neighbor)

        res=0
        for node in range(n):
            if not visited[node]:
                res+=1
                visited[node]=True
                dfs(node)
        return res 
