class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if(len(intervals) == 1):
            return intervals
        
        intervals = sorted(intervals,key = lambda x : x[0])

        results = []
    
        current_start = intervals[0][0]
        current_end = intervals[0][1]
        
        for start,end in intervals[1:]:
            if(start > current_end):
                results.append([current_start,current_end])
                current_start = start
                current_end = end
                
            else:
                current_end = max(current_end,end)
                
        results.append([current_start,current_end])
        
        return results
        
        
        
        
#         if(len(intervals) == 1):
#             return intervals
        
#         intervals = sorted(intervals, key = lambda x: x[0])
        
#         res = [intervals[0]]
    
        
#         for i in intervals[1::]:
#             if(i[0] <= res[-1][1]):
#                 res[-1][0] = min(res[-1][0],i[0])
#                 res[-1][1] = max(res[-1][1],i[1])
#             else:
#                 res.append(i)
                
#         return res
            