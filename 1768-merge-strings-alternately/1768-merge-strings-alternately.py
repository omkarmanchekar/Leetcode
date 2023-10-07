class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
#         min_length = min(len(word1),len(word2))
        
#         res = ''
#         for i in range(min_length):
#             res = res + word1[i] + word2[i]
            
#         if(len(word1) > len(word2)):
#             res = res + word1[min_length:]
#         else:
#             res = res + word2[min_length:]
            
#         return res
    
    
        lenght_word1 = len(word1)
        lenght_word2 = len(word2)
        
        i = 0
        j = 0
        
        res = ''
        
        while(i < lenght_word1 or j < lenght_word2):
            if(i < lenght_word1):
                res = res + word1[i]
                i = i+1
            if(j < lenght_word2):
                res = res + word2[j]
                j = j+1
                
        return res