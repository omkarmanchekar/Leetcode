class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
#Brute force approach
        
#         res = [0] * len(temperatures)
        
#         for i in range(len(temperatures)):
#             for j in range(i,len(temperatures)):
#                 if(temperatures[j]>temperatures[i]):
#                     res[i] = (j-i)
#                     break
#         return res

# MONOTONIC STACK approach (without referring sol )

        res = [0] * len(temperatures)

        i = 0
        mono = []
        while(i < len(temperatures)):
            if(len(mono) == 0):
                mono.append((temperatures[i],i))  
            else:
                if(temperatures[i] > mono[-1][0]):
                    while(mono and mono[-1][0] < temperatures[i]):
                        val,ind = mono.pop(-1)
                        res[ind] = i-ind
                mono.append((temperatures[i],i))
            i +=1
    
    
        return res
                    
            