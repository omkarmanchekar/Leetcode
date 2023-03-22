class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        
        relations = collections.defaultdict(set)
        in_edge = collections.defaultdict(int)
        
        
#         unique letters
        unique = collections.Counter("".join(words)).keys()
            
        for i in unique:
            relations[i]
            in_edge[i] = 0 
            
        for i in range(len(words)-1):
            first = words[i]
            second = words[i+1]
            
            for x,y in zip(first,second):
                if(x != y ):
                    if(y not in relations[x]):
                        relations[x].add(y)
                        in_edge[y] +=1
                    break
                        
                        
            else:
                if(len(second) < len(first)):
                    return ""
            
        
        queue = [x for x in unique if in_edge[x] == 0]
        result = []
        
        while(queue):
            top = queue.pop(0)
            result.append(top)
            
            for i in relations[top]:
                in_edge[i] -= 1
                if(in_edge[i] == 0):
                    queue.append(i)
                    
        if(len(result) < len(unique)):
            return ""
        
        return "".join(result)
        
        
            
            

#         unique = collections.Counter("".join(words)).keys()
#         l = collections.defaultdict(set)
#         count = collections.defaultdict(int)
        
#         for i in unique:
#             l[i]
#             count[i]
        

#         for i in range(len(words)-1):
            
#             if(words[i+1] == words[i][:len(words[i+1])]):
#                 if(len(words[i+1]) >= len(words[i]) ):
#                     continue
#                 elif(len(words[i+1]) < len(words[i])):
#                     return ''


#             index = 0
#             while(words[i][index] == words[i+1][index]):
#                 index+=1

                
#             if(words[i+1][index] not in l[words[i][index]]):
#                 # count[words[i+1][index]].add(words[i][index])
#                 count[words[i+1][index]] +=1 
                
                
#             l[words[i][index]].add(words[i+1][index])
            
            
            
#         queue = []
        
#         for i in count:
#             if(count[i] == 0):
#                 queue.append(i)
                
#         # print(queue)
#         res = []
        
#         while(queue):
#             top = queue.pop(0)
#             res.append(top)
#             for i in l[top]:
#                 count[i] -=1
#                 if(count[i] == 0):
#                     queue.append(i)
                    
#         if(len(res) < len(unique)):
#             return ""
        
#         return "".join(res)
                
            
            
#         print(l,count)
                