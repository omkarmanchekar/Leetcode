class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        
        hash = {"(":")","{":"}","[":"]"}
        
        for i in s:
            if(i in hash):
                stack.append(i)
            else:
                if(len(stack) == 0):
                    return False
                else:
                    if(i == hash[stack[-1]]):
                        stack.pop()
                    else:
                        return False
                    
        if(len(stack) == 0):
            return True 
        else:
            return False