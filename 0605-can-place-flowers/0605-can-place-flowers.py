class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        possible_place = 0
        
        for i in range(len(flowerbed)):
            
            if(flowerbed[i] == 0):
                
                is_left_empty = (i==0) or (flowerbed[i-1] == 0)
                is_right_empty = (i == len(flowerbed)-1) or(flowerbed[i+1] == 0)
                
                if(is_left_empty and is_right_empty):
                    flowerbed[i] = 1
                    possible_place +=1
                    
        return possible_place >= n