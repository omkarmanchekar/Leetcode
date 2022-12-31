class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        if(obstacleGrid[0][0] == 1):
            return 0
        
        
        dp = [[0] * col for _ in range(row)]
        
        dp[0][0] = 1
        
        for i in range(1,col):
            if(obstacleGrid[0][i] == 0 and dp[0][i-1] == 1):
                dp[0][i]=1
            
        for i in range(1,row):
            if(obstacleGrid[i][0] == 0 and dp[i-1][0] == 1):
                dp[i][0] = 1    

        
        for r in range(1,row):
            for c in range(1,col):
                if(obstacleGrid[r][c] == 0):
                    dp[r][c] = dp[r-1][c]  + dp[r][c-1]
                else:
                    dp[r][c] = 0
                    

                    
        return dp[row-1][col-1]