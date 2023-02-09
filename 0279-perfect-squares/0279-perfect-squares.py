class Solution:
    def numSquares(self, n: int) -> int:
        
        
        square = [i*i for i in range(1,int(n**0.5)+1)]
        
#BFS approach will give TLE when number is big 
        
#         queue = collections.deque([(n,0)])
#         while(queue):
#             val,distance = queue.popleft()
#             if(val == 0):
#                 return distance
            
#             for i in square:
#                 if((val-i) >= 0):
#                     queue.append((val-i,distance+1))
                    
            
        
        dp = [float('inf')] * (n+1)
        
        dp[0] = 0
        
        for i in range(1,n+1):
            for s in square:
                if(s > i):
                    break
                dp[i] = min(dp[i-s]+1,dp[i])
        
        return dp[-1]
        
        