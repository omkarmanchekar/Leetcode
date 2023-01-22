class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = 0
        unique = 1
        nex = 1
        
        while(nex < len(nums)):
            if(nums[nex] != nums[curr]):
                curr += 1 
                nums[curr] = nums[nex]
                unique +=1
            nex+=1
            
        return unique