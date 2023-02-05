class Solution:
    def rob(self, nums: List[int]) -> int:
#         Top-bottom (Recursive approach)

        def dp(i):
            
            if(i == 0):
                return nums[0]
            if(i == 1):
                return max(nums[0],nums[1])
            if(i not in hash):
                hash[i] = max(dp(i-1),dp(i-2) + nums[i])
        
            return hash[i]
        
        hash = {}
        return dp(len(nums)-1)
        
        
#         Bottom-top (iterative approach)

#         if(len(nums) == 1):
#             return nums[0]
        
#         dp = [0] * len(nums)
        
#         dp[0] = nums[0]
#         dp[1] = max(nums[0],nums[1])
        
#         for i in range(2,len(nums)):
#             dp[i] = max(nums[i] + dp[i-2],dp[i-1])
            
        
#         return dp[-1]