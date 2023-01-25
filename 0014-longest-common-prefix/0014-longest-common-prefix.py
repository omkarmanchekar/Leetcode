class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        res = ""
        
        l = list(zip(*strs))
        
        for i in l:
            if(len(set(i)) == 1):
                res += i[0]
            else:
                break
                
        return res