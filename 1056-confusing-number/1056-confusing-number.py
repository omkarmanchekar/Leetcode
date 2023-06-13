class Solution:
    def confusingNumber(self, n: int) -> bool:
        confusingNumber = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
        
        
        num = str(n)
        res = ''
        
        for i in num:
            if(i not in confusingNumber):
                return False
            res = res + confusingNumber[i]
            
        print(res)
       
        if(int(res[::-1]) == n):
            return False
        else:
            return True 
        