class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        
        for i in list(s):
            if len(stack) and i == "*":
                stack.pop()
                continue
                
            stack.append(i)
            
        return "".join(stack)
                