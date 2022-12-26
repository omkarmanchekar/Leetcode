class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        @cache
        def dp(i,left):
            if(i == m):
                return 0
            right = n-1-(i-left)
            mul = multipliers[i]
            res = max(mul*nums[left]+dp(i+1,left+1),mul*nums[right] + dp(i+1,left))
            return res
        
        n,m = len(nums),len(multipliers)
        return dp(0,0)
        