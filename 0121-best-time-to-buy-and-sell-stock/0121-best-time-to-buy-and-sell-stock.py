class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        current = float('inf')
        
        best = 0
        
        
        for i in prices:
            current = min(current,i)
            best = max(best,i-current)
            
            
        return best 