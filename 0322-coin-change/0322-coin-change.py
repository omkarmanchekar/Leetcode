class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if(amount == 0):
            return 0
        
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        
        for i in range(amount):
            for j in coins:
                if(i+j <= (amount)):
                    dp[i+j] = min(dp[i] + 1,dp[i+j])
                
        return dp[amount] if dp[amount] != float('inf') else -1
                
            