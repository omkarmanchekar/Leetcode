class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        """Does not work for -1,-1,-1,-1,-1,-1,0"""

        # left = 0 
        # right = len(nums) -1 

        # l = nums[0]
        # r = nums[-1]

        # while left != right:
        #     if l <= r:
        #         left +=1
        #         l += nums[left]
        #     elif r < l:
        #         right -=1
        #         r += nums[right]

        
        # if l == r:
        #     return left
        # return -1


        """
        take O(n) space with o(n) time, space can be improved
        """
        
        # left = nums.copy()

        # for i in range(1,len(left)):
        #     left[i] = left[i-1] + left[i]

        # right = nums.copy()
        # for i in range(len(right)-2,-1,-1):
        #     right[i] = right[i+1] + right[i]


        # for i in range(len(nums)):
        #     if right[i] == left[i]:
        #         return i

        # return -1


        """
        Spcae O(1)
        """

        right = sum(nums)

        left = 0

        for index,value in enumerate(nums):
            if left == right-left-value:
                return index
            left += value 

        return -1
       