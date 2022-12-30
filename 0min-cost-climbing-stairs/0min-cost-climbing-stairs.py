class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
#         dp = [0] * len(cost)
        
#         dp[0] = cost[0]
#         dp[1] = cost[1]
        
#         for i in range(2,len(cost)):
#             dp[i] = min(dp[i-1],dp[i-2]) + cost[i]
            
            
#         return min(dp[-1],dp[-2])
    
    
#     Reducting State hence reducing complexity 
        dp  = [0] * len(cost)
        
        first_elem = cost[0]
        second_elem = cost[1]
        
        for i in range(2,len(cost)):
            temp = min(first_elem,second_elem) + cost[i]
            first_elem,second_elem = second_elem, temp
            
        return min(first_elem,second_elem)
        
    