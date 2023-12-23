class Solution:
    def compress(self, chars: List[str]) -> int:
        
        i = 0
        res = 0


        while i < len(chars):
            element = chars[i]
            count  = 1
            while i+1 < len(chars) and chars[i+1] == element:
                count += 1
                i +=1
            
            if count >1:
                group = element + str(count)
                group_list = [*group]
                chars[res:res+len(group_list)] = group_list
                res += len(group_list)
            else:
                chars[res:res+1] = element
                res +=1
            
            i+=1


        return res



        




