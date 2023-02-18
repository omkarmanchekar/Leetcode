class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
#         Brute force O(n^2)
#         Sorting O(nlogn)



#         hash table O(n)        
        counter = collections.defaultdict(int)
        
        for i in nums:
            if(counter[i] == 1):
                return True
            
            counter[i] = 1
            
        return False