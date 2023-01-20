class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if(source == destination):
            return True
        
        
        graph  = collections.defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        # print(graph)
            
        
        visited = [0] * (n)
        # visited.append(source)
        
        # print("root visited   ",visited)
        
        
        # def dfs(source,visited,graph,destination):
        #     for v in graph[source]:
        #         print("list of element   ",graph[source])
        #         if(v not in visited):
        #             if(v == destination):
        #                 print("==============")
        #                 return True
        #             else:
        #                 visited.append(v)
        #                 print("Inside visited. ",visited)
        #                 dfs(v,visited,graph,destination)
        #                 return False
        #     print("----------------")
        #     # return False
        
        res = False
        
        def dfs(source,visited,graph,destination):
            if(source == destination):
                return True
            
            if(visited[source] == 0):
                visited[source] = 1
                for v in graph[source]:
                    # print("list of element   ",graph[source])
                    # if(v not in visited):
                    #     if(v == destination):
                    #         print("==============")
                    #         return True
                    #     else:
                    #         visited.append(v)
                    #         print("Inside visited. ",visited)
                    res = dfs(v,visited,graph,destination)
                    if res:
                        return True 

        
        return dfs(source,visited,graph,destination)
                
            
        
        