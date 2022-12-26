class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # @lru_cache(maxsize = None)
        @cache
        def dp(i,j):
            if(i ==  n or j ==  m):
                return 0
        
            if(text1[i] == text2[j]):
                return (1 + dp(i+1,j+1))
            
            return max(dp(i+1,j), dp(i,j+1))
        
        
        
        
        n, m = len(text1),len(text2)
        
        return dp(0,0)