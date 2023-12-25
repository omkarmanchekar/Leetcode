class Solution:
    def maxArea(self, height: List[int]) -> int:

        """
        basic simple first logic (Brute force) O(n^2)
        """

        # max_water = 0
        # for left in range(len(height)-1):
        #     for right in range(left+1,len(height)):
        #         distance = right-left
        #         height_container = min(height[left],height[right])
        #         max_water = max(max_water,distance * height_container)


        # return max_water

        """
        two pointer appaorch 
        """
        left = 0
        right = len(height)-1

        max_water = 0
        
        while left < right:
            current_water = (right-left) * min(height[left],height[right]) 
            max_water = max(max_water,current_water)

            if height[left] <= height[right]:
                left +=1
            else:
                right-=1

        return max_water

        


        