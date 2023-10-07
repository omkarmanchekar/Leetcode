class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
#         GCD has to be prefix common string in both the strings 
#         so take the smallest one as GDC for brute force method

        len1 = len(str1)
        len2 = len(str2)
        
        base = str1[:min(len1,len2)]
        
        while(base):
            if(len1 % len(base) == 0 and len2 % len(base) == 0):
                if((len1//len(base)) * base == str1 and (len2//len(base))* base == str2):
                    return base
                
            base  = base[:-1]
            
        return ''