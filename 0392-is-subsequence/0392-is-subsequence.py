class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s == "":
            return True
        
        first = 0
        second = 0
        
        count = len(s)
        
        while second < len(t) and first < len(s):
            if(s[first] == t[second]):
                first +=1 
                count -=1
            
            second += 1
            if(count == 0):
                return True
        
        
        return False