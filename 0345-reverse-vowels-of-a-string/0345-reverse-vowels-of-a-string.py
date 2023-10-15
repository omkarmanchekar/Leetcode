class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        
        s = list(s)
        
        v = [i for i in s if i in vowels]
        
        v = v[::-1]
        
        c = 0
        
        
        for i in range(len(s)):
            if(s[i] in vowels):
                s[i] = v[c]
                c+=1
                
                
        return ''.join(s)