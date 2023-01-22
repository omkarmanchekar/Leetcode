class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
            
        # DFS approach 
        # graph  = collections.defaultdict(list)
#         for u,v in edges:
#             graph[u].append(v)
#             graph[v].append(u)
            
#         visited = [0] * (n)
        
#         res = False
        
#         def dfs(source,visited,graph,destination):
#             if(source == destination):
#                 return True
            
#             if(visited[source] == 0):
#                 visited[source] = 1
#                 for v in graph[source]:
#                     res = dfs(v,visited,graph,destination)
#                     if res:
#                         return True 

        
#         return dfs(source,visited,graph,destination)
                
        # BFS approach 
        
        graph = collections.defaultdict(list)
        for s,d in edges:
            graph[s].append(d)
            graph[d].append(s)
            
        queue = []
        queue.append(source)
        
        visited = [False] * n

        while(queue):
            top = queue.pop()
            if(top == destination):
                return True 
            visited[top] = True
            
            for i in graph[top]:
                if(visited[i] == False):
                    visited[i] = True 
                    queue.append(i)
                    
            
        return False
            
            
            
        
        
        