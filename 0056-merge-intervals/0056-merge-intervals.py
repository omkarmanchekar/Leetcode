class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if(len(intervals) == 1):
            return intervals
        
        intervals = sorted(intervals, key = lambda x: x[0])
        
        res = [intervals[0]]
    
        
        for i in intervals[1::]:
            if(i[0] <= res[-1][1]):
                res[-1][0] = min(res[-1][0],i[0])
                res[-1][1] = max(res[-1][1],i[1])
            else:
                res.append(i)
                
        return res
            