from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = defaultdict(int)
        
        for i in arr:
            counter[i] +=1 
            
        return len(list(counter.values())) == len(set(counter.values()))
        
        
            