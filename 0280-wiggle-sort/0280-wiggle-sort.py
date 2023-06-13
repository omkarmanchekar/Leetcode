class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
  
        nums.sort()
    
        # print(nums)
    
        for i in range(1,len(nums)-1,2):

            nums[i+1],nums[i] = nums[i],nums[i+1]
#             temp = nums[i]
#             nums[i] = nums[i+1]
#             nums[i+1] = temp
            
            
            
        
            