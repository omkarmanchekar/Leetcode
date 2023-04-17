class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals,key = lambda x :x[1])
        print(intervals)
        
        count = 0
        
        current_start = intervals[0][0]
        current_end = intervals[0][1]
        
        for start,end in intervals[1:]:
            if(start < current_end):
                count +=1 
            else:
                current_end = end 
                current_start = start
                
        return count