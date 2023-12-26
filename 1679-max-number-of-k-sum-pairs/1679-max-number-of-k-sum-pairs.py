class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        
        """
        Brute force
        """
        # res = 0

        # for first in range(len(nums)-1):
        #     if nums[first] == 0:
        #         continue
        #     for second in range(first+1,len(nums)):
        #         if nums[second] == 0:
        #             continue
        #         if nums[first] + nums[second] == k:
        #             nums[first] = nums[second] = 0
        #             res +=1 
        #             break

        # return res

        """
        Two pointer with sorting of the list
        """

        nums = sorted(nums)

        left = 0
        right = len(nums)-1 
        res = 0


        while left< right:
            if(nums[left] + nums[right] == k):
                res +=1 
                left+=1
                right-=1
            elif nums[left] + nums[right] > k:
                right-=1
            else:
                left+=1

        return res





            