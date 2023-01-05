class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        nodes = []
        edges = []
        
        n  = len(isConnected)
        
        for i in range(n):
            for j in range(n):
                if(isConnected[i][j] == 1):
                    if(i == j):
                        nodes.append(i+1)
                    else:
                        edges.append([i+1,j+1])
                        
                
            
            
        def dfs(node,edges,visited):
            visited[node] = 1
            for i,j in edges:
                if(i == node and visited[j] == 0):
                    dfs(j,edges,visited)

                        
        visited = [0] * (n+1)
        res = 0
        
        for i in nodes:
            if(visited[i] == 0):
                dfs(i,edges,visited)
                res += 1 
                
                
        return res
        
        
        
                    