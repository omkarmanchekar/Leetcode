class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if(len(prerequisites) == 0):
            return True 
        
        pre = collections.defaultdict(list)
        
        for i in prerequisites:
            pre[i[1]].append(i[0])
            
        path = [False] * numCourses
        
        visitedOnce = [False] * numCourses
        
        
        def checkCycle(course):
            
            if(visitedOnce[course]):
                return False
            
            if(path[course]):
                return True
            
            path[course] = True 
            isCycle  = False
            
            for i in pre[course]:
                isCycle = checkCycle(i)
                if(isCycle):
                    return True
                
            path[course] = False
            visitedOnce[course] = True
            return isCycle
            
            
            
        for i in list(pre):
            if(checkCycle(i)):
                return False
            
        return True
        
