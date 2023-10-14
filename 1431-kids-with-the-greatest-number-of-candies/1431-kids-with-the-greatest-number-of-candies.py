class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_cad = max(candies)
        
        
        res = []
        
        for c in candies:
            if(c + extraCandies >= max_cad):
                res.append(True)
            else:
                res.append(False)
                
                
        return res