class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        """
        ~  first we will iterate over the list from 0 to len(nums)-3 because if list is less then 3 does not 
            makes sense hence edge case that can be handled initially 
        ~ counter will keep track of how many valid numbers are found till now we have to do it until 
            counter  is 3  
        ~ first element will always be the largest and the counter will be one 1, when iterating if you find a 
            element greater than the largest new largest will be this element and counter will increase as 2
            do this untill counter becomes 3 if counter becomes 3 that mean you have the sequence you want
       
        # Fails when 0,4,1,3 
        # first largest = 0, second largest = 4 which should update to 1 as 1 > 0 

        """
        # for i in range(len(nums)-3):
        #     largest  = nums[i]
        #     counter = 1
        #     for j in range(i+1,len(nums)):
        #         if(nums[j] > largest):
        #             largest = nums[j]
        #             counter += 1
            
        #     if(counter >= 3):
        #         return True
        
        # return False  


        """ 
        Second approach is to do double scan and get left min list and in second scan get max right list, 
        for ith element if max [i+1] >i > min[i-1] then true 
        but space complexity is O(n) 
        """

        """
        But can be solved in O(1) space as per solution
        this can also handles edge case of len < 3, 1,2,0,3
        first = 1
        second = 2
        first = 0
        third= 3
        """

        first = second = float("inf")

        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True 

        return False 



