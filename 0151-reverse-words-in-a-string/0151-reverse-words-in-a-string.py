class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(filter(lambda x : x != '',s.split(' ')))
        
        
        s = s[::-1]
        return ' '.join(s)
    