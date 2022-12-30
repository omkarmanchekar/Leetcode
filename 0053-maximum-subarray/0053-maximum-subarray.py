class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
#         kadane algorithm
# keeps track of running sum and at any point if running sum is less that the current element it replaces the current element with running sum
        
        best  = float('-inf')
        
        current  = 0
        
        for i in nums:
            current = max(current + i, i)
            best = max(best,current)
            
            
        return best