class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        n = len(jobDifficulty)
        
        if(n < d):
            return -1
        
        
        @lru_cache(maxsize = None)
        
        def dp(i,day):
            if(day == d):
                return max(jobDifficulty[i:])
            best = float('inf')
            
            for j in range(i,n-(d-day)):
                max_difficulty_of_day = max(jobDifficulty[i:j+1])
                best = min(best,max_difficulty_of_day + dp(j+1,day+1))
                
            
            
            return best
            
            
        
        return dp(0,1)