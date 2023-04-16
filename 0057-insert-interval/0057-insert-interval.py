class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if(len(intervals) == 0):
            return [newInterval]
        
        result  = []
        
        for i in range(len(intervals)):
            if(newInterval[0] < intervals[i][0]):
                intervals.insert(i,newInterval)
                break
        else:
            intervals.insert(len(intervals),newInterval)

        print(intervals)
        current_start = intervals[0][0]
        current_end = intervals[0][1]
        
        for start,end in intervals[1:]:
            if(start > current_end):
                result.append([current_start,current_end])
                current_start = start
                current_end = end
            
            else:
                current_end = max(current_end,end)
            
        result.append([current_start,current_end])
        
        return result
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         intervals.append(newInterval)
        
#         intervals  = sorted(intervals,key = lambda x:x[0])
        
#         print(intervals)
#         res = []
        
#         index = 0
        
#         while(index < len(intervals)):
#             start,end = intervals[index]
#             print(start,end)
            
#             while(intervals[index+1] and intervals[index+1][0] <= end ):
#                 print("11   ",index,index+1)
#                 start = min(start,intervals[index+1][0])
#                 end = max(end,intervals[index+1][1])
#                 print(start,end)
#                 index = index  + 1
                
                
#             res.append([start,end])
#             index += 1
        
#         print(intervals,res)