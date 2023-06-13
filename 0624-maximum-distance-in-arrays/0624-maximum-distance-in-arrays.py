class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minv = arrays[0][0]
        maxv = arrays[0][-1]
        res = 0
        for i in range(1,len(arrays)):
    
    
            res = max(res,max(abs(minv-arrays[i][-1]),abs(maxv-arrays[i][0])))
            minv = min(minv,arrays[i][0])
            maxv = max(maxv,arrays[i][-1])
            
        return res