class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        
#         Brute force O(n^2)

#       Similar to maximum subarray but also need to keep track of min (bcz of negative value)

        minimum = maximum = nums[0]
    
        res = nums[0]
    
        for i in range(1,len(nums)):
        
            maxxx = max(nums[i],max(minimum * nums[i],maximum * nums[i]))
            minimum = min(nums[i],min(minimum * nums[i],maximum * nums[i]))
            
            maximum = maxxx
            
            res = max(maximum,res)
            
        return res
            