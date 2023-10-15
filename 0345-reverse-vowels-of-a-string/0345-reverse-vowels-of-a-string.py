class Solution:
    def reverseVowels(self, s: str) -> str:
#         vowels = ['a','e','i','o','u','A','E','I','O','U']
#         s = list(s)
#         v = [i for i in s if i in vowels]
#         v = v[::-1]
#         c = 0
#         for i in range(len(s)):
#             if(s[i] in vowels):
#                 s[i] = v[c]
#                 c+=1
                   
#         return ''.join(s)
    
    
#     Two pointer 

        vowels = ['a','e','i','o','u','A','E','I','O','U']
    
        if(len(s) == 1):
            return s
    
        s = list(s)
        
        
        left = 0
        right = len(s)-1
        
        while(left <= right):
            
            while(s[left] not in vowels and left < len(s)-1):
                left +=1
            
            while(s[right] not in vowels and right > 0):
                right-=1
                
                
            print(left,right)
            if(left <= right):
                s[left],s[right] = s[right],s[left]
                left +=1 
                right-=1
            
            
        return ''.join(s)
    