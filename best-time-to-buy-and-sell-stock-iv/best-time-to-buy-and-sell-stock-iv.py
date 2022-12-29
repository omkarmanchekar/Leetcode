class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @lru_cache(maxsize = None)
        def dp(i,transactionRemaining,holding):
            if(transactionRemaining == 0 or i == len(prices) ):
                return 0
            
            if(holding):
                return max(dp(i+1,transactionRemaining,holding),prices[i] + dp(i+1,transactionRemaining-1,0))
            else:
                return max(dp(i+1,transactionRemaining,holding),-prices[i] + dp(i+1,transactionRemaining,1))                
            
        
        return dp(0,k,0)