class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        """
        set left and right as 0 initialy,
        iterate right through list 
        if right is 1 ignore continue 
        if right is 0 k--
        if k is positive the window is still valid keep increasing right pointer 
        once k goes less than 0 
        we have window which is valid and max till now, we will keep the window size same but will move left by one irrespective of the left value 
        so if left is 1 dont do anything just increase the pointer of left 
        if left is 0 k++, as so as k > 0 we can add 0 as valid window and extend right keeping left same  
        """
        
        left = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                k -=1
            
            if k < 0:
                if nums[left] == 0:
                    k+=1
                left +=1 
                
        return (right-left+1)

