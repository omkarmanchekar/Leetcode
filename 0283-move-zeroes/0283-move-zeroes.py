class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       
        """
        basic approach create a new array, append all the non zero first and 
        keep count of zeros, which can be append at the end 
        """
        # res = []
        # numberOfZero = 0
        # for i in nums:
        #     if i == 0:
        #         numberOfZero +=1
        #     else:
        #         res.append(i)
        # while numberOfZero:
        #     res.append(0)
        #     numberOfZero -=1
        # for i in range(len(nums)):
        #     nums[i] = res[i]

        """
        Second approach two pointer, fast and slow pointer approach 
        slow pointer is to set all non zero intergers found at the start of
        list, until the fast counter reaches end of he list, once the fast 
        pointer reaches the end start to replace all the elements after slow
        pointer as zero 
        """

        slow = 0
        
        for i in nums:
            if i != 0:
                nums[slow] = i
                slow +=1 
            
        for i in range(slow,len(nums)):
            nums[i] = 0

        
        




