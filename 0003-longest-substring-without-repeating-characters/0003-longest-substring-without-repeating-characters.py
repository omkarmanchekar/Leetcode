class Solution:
    
#     BRUTE FORCE APPROACH 
#     def checkUnique(self,s):
#         counter= collections.defaultdict(int)
#         for i in s:
#             if(i in counter):
#                 return False
#             counter[i] += 1
        
#         return True 
    
    
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         res = 0
#         for i in range(len(s)):
#             for j in range(i,len(s)):
#                 if(self.checkUnique(s[i:j+1])):
#                     res = max(res,len(s[i:j+1]))
                    
#         return res
                
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) == 0):
            return 0
        
        unique = [0] * 128
    
        left = 0
        right = 1
        
        unique[ord(s[0])] = 1
        res = 1
        
        while(right < len(s)):
            if(unique[ord(s[right])] == 0):
                res = max(res,len(s[left:right+1]))
                unique[ord(s[right])] = 1
                right +=1 
            else:
                unique[ord(s[left])] = 0
                left += 1
            
            
        return res
            
            
            
            
                