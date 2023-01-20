class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # if(source == destination):
        #     return True
        
        graph  = collections.defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = [0] * (n)
        
        res = False
        
        def dfs(source,visited,graph,destination):
            if(source == destination):
                return True
            
            if(visited[source] == 0):
                visited[source] = 1
                for v in graph[source]:
                    res = dfs(v,visited,graph,destination)
                    if res:
                        return True 

        
        return dfs(source,visited,graph,destination)
                
            
        
        