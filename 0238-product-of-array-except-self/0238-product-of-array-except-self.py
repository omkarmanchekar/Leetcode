class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
        """
        # brute force approach would be to traverse the list twice
        # time complexity is O(n^2)

        result = [0] * len(nums)
        for i in range(len(nums)):
            product  = 1
            for j in range(len(nums)):
                if(j == i):
                    continue
                product *= nums[j]

            result[i] = product

        return result 
        """    

        # for each index we need product from that index to end and product from first to that index-1
        # can be done using precomputed product list, example precomputed product list from left to right and other from right to left 

        # need something to handle the case with len(nums) ==1 
        if(len(nums) < 2):
            return nums

        left_right = nums.copy()
        right_left = nums.copy()

        for i in range(1,len(left_right)):
            left_right[i] = left_right[i-1] * left_right[i]
            # this will break when the nums is of lenght 1

        for i in range(len(right_left)-2,-1,-1):
            print(i)
            right_left[i] = right_left[i+1] * right_left[i]

        print(left_right,right_left)


        for i in range(len(nums)):
            if(i == 0):
                nums[i] = right_left[i+1]
            elif(i == len(nums)-1):
                nums[i] = left_right[i-1]
            else:
                nums[i] = left_right[i-1] * right_left[i+1]

        return nums

    
        """
        Can be improved/less complicated
        left = [1] * len(nums)
        right = [1] * len(nums)
        
        for i in range(1,len(nums)):
            left[i] = left[i-1] * nums[i-1]
            
        for j in range(len(nums)-2,-1,-1):
            right[j] = right[j+1] * nums[j+1]
            
    
        res = [0] * len(nums)
        
        for i in range(len(nums)):
            res[i] = left[i] * right[i]
            
        return res
        """

        


       
                