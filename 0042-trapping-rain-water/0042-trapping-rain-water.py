class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        left = []
        right  = []
        max_val = 0
        res = 0
        
        for i in height:
            left.append(max(max_val,i))
            max_val = max((max_val,i))
        
        max_val = 0
        
        for i in height[::-1]:
            right.insert(0,max(max_val,i))
            max_val = max((max_val,i))
            

        for i in range(len(height)):
            res+= (min(left[i],right[i]) - height[i])
            
        return res
    
# Brute force is to iterate through each and look to left and right max inclusive of that element check for min and subtract element 