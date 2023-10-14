class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if(str1 + str2 != str2 + str1):
            return ''
    
        s1 = len(str1)
        s2 = len(str2)
        
        base = str1[:min(s1,s2)]
        
        while(base):
            if(s1%len(base) == 0 and s2%len(base) == 0):
                k1 = s1 // len(base)
                k2 = s2 // len(base)
                if(k1*base == str1 and k2* base == str2):
                    return base
                
            base = base[:-1]
            
        return ''
            
            
            
