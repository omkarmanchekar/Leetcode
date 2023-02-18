class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
#         Brute Force 
#         res = 0
#         for i in range(len(prices)):
#             for j in range(i,len(prices)):
#                 if(prices[j] > prices[i]):
#                     res = max(res,prices[j]-prices[i])
                    
#         return res
    
    
#     find the lowest point and keep checking for max profit in single pass 
        minn = float('inf')
        maxx = 0
        
        for i in range(len(prices)):
            minn = min(minn,prices[i])
            maxx = max(maxx,prices[i] - minn)
            
        return maxx
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         modified kanade algorithm as kanade is mostly used when there are negative elements in input 
        
#         current = float('inf')
        
#         best = 0
        
        
#         for i in prices:
#             current = min(current,i)
#             best = max(best,i-current)
            
            
#         return best 