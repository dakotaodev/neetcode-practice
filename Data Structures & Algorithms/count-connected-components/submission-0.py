class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj:list[list]=[[] for _ in range(n)]
        visited=[False]*n

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(n):
            
            neighbors=adj[n]
            for n in neighbors:
                if not visited[n]:
                    visited[n]=True
                    dfs(n)

        res=0
        for node in range(n):
            if not visited[node]:
                res+=1
                visited[node]=True
                dfs(node)
        
        return res