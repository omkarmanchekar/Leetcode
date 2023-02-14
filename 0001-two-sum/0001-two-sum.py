class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i,j]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         remainder = {}
#         for i in range(len(nums)):
#             if(nums[i] in remainder):
#                 return remainder[nums[i]],i
            
#             remainder[target-nums[i]] = i
        