class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        visited=[False]*n

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node):
            
            visited[node]=True
            for n in adj[node]:
                if not visited[n]:
                    dfs(n)
            
        res=0
        for i in range(n):
            if not visited[i]:
                res+=1
                visited[i]=True
                dfs(i)
        return res