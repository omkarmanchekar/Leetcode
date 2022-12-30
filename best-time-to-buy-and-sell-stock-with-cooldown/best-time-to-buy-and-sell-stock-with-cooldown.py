class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(maxsize = None)
        def dp(i,holding):
            if(i == len(prices) ):
                return 0
        
            if(i == len(prices)-1 and holding):
                return prices[i]
            
            if(holding):
                return max(dp(i+1,holding),prices[i] + dp(i+2,0))
            else:
                return max(dp(i+1,holding),-prices[i] + dp(i+1,1))
            
            
        return dp(0,0)