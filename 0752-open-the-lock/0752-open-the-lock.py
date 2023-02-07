class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        queue = collections.deque([])
        
        queue.append(("0000",0))
        
        visited = set(deadends)
#         if("0000" in visited):
#             return -1
        
        # visited.add("0000")
        
        
        def getlistofnext(node):
            res = []
            for i in range(4):
                val = int(node[i])
                res.append(node[:i] + str((val+1)%10) + node[i+1:])
                res.append(node[:i] + str((val-1)%10) + node[i+1:])
                
            return res
        
        
        while(queue):
            val,distance = queue.popleft()
            
            if(val == target):
                return distance
            if(val in visited):
                continue
            for node in getlistofnext(val):
                if(node not in visited):
                    
                    queue.append((node,distance+1))
            visited.add(val)
            
        return -1
                    
        