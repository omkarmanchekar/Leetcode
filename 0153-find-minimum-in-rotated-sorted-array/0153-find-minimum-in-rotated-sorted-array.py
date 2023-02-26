class Solution:
    def findMin(self, nums: List[int]) -> int:

        '''
Brute force approach:

Sort and return first O(nlogn)
Traverse through whole array O(n)

'''

#  Use divide and conquer O(logn)

            
        if(len(nums) == 1):
            return nums[0]

        if(len(nums) == 2):
            return min(nums)

        mid = len(nums)//2
        
# if the list is already sorted just return first 
        if(nums[-1] > nums[0]):
            return nums[0]
        
# else check mofdified binary search 
        if(nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]):
            return nums[mid]

        if(nums[0] < nums[mid]):
            return self.findMin(nums[mid+1:])
        else:
            return self.findMin(nums[:mid])
                
        