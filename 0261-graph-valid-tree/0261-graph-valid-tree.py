
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if(len(edges) != n-1):
            return False
        
        
        relation = collections.defaultdict(set)
        
        
        for i,j in edges:
            relation[i].add(j)
            relation[j].add(i)
        
        visited =set()
        queue = [0]
        
        while(queue):
            node = queue.pop(0)
            visited.add(node)

            for i in relation[node]:
                if(i in visited):
                    continue
                queue.append(i)

        
            
        return len(visited) == n
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if(len(edges) > n-1 or len(edges) < n-1):
#             return False
        
#         if(n == 1 and len(edges) == 0):
#             return True
#         new = []
#         for i in edges:
#             new.append(sorted(i))
        
#         # print(new)
        
#         sorted_edges = sorted(new,key = lambda x:x[0])
#         print(sorted_edges)
        
#         root = sorted_edges[0][0]
        
#         visited = [0] * n
        
#         res = True
        
#         def dfs(node,visited,sorted_edges):
#             visited[node] = 1
#             for i,j in sorted_edges:
#                 print("node",node, " ","i",i)
#                 # print("ssss" ,visited)
#                 if(i == node and visited[j] == 0):
#                     if(visited[j] == 0):
                        
#                         print(i,j)
#                         print(visited)
#                         print("  ")
#                         dfs(j,visited,sorted_edges)
                    
#                     else:
#                         print("res")
#                         # res = False
#                         return False
#                         # break
                        
                
#             print("res222",visited)
#             if(sum(visited) != n):
#                 return False
#             else:  
#                 return True 
            
#         return dfs(root,visited,sorted_edges)
        
        
#         # if(sum(visited) == n+1):
#         # return res
    
    