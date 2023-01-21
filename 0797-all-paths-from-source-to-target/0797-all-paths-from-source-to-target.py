class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end = len(graph)-1
        
        result = []
        
        def dfs(source,graph,destination,path,result):
            
            if(source == destination):
                result.append(list(path))
                return 
                
            for v in graph[source]:
                path.append(v)
                dfs(v,graph,destination,path,result)
                path.pop()
                    
                    
        path = [0] 
        dfs(0,graph,end,path,result)
        return result

                