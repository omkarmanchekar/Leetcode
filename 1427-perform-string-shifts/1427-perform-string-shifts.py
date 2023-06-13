class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        for direction,amount in shift:
            counter = amount
            while(counter):
                if(direction):
                    s = s[-counter:] + s[:-counter]
                else:
                    s = s[counter:]+s[:counter] 
                
                if(len(s) < counter):
                    counter = counter - len(s)
                else:
                    counter = 0  
        
        return s