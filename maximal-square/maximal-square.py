class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        rows,cols = len(matrix),len(matrix[0])
        
        dp =[]
        
        res = 0
        
        for i in range(rows):
            dp.append([0]*cols)
            

        for j in range(cols):
            dp[0][j] = int(matrix[0][j])
            res = max(res,dp[0][j])
                
        for i in range(rows):
            dp[i][0] = int(matrix[i][0])
            res= max(res,dp[i][0])
                
        # print(dp)
            
        for i in range(1,rows):
            for j in range(1,cols):
                # print(i,j)
                if(matrix[i][j] == "1"):
                    dp[i][j] = min(min(dp[i-1][j],dp[i][j-1]),dp[i-1][j-1]) + 1
                    res = max(res,dp[i][j])
                
        return res*res