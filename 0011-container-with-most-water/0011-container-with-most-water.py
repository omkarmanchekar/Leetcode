class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        Brute Force O(N^2)
        
        '''
        
        left = 0
        right = len(height) -1 
        
        
        res = min(height[left],height[right]) * (right-left)
        while(left < right):
            if(height[left] <= height[right] ):
                left+=1
                res = max(res,min(height[left],height[right]) * (right-left))
            else:
                right -=1
                res = max(res,min(height[left],height[right]) * (right-left))
            
            
        return res