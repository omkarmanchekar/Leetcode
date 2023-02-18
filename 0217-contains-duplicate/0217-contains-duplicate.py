class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        counter = collections.defaultdict(int)
        
        for i in nums:
            if(counter[i] == 1):
                return True
            
            counter[i] = 1
            
        return False