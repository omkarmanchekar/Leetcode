class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        '''
        Traversing list O(n)
        '''
        
        start = 0
        end = len(nums)-1
        
        while(start<= end):
            mid = (start + end)//2
            print("mid ",start,end,mid,nums[mid])
            
            if(nums[mid] == target):
                print("1")
                return mid
            
            elif(nums[mid] >= nums[start]):
                if(target <= nums[mid] and target >= nums[start]):
                    print("2")
                    end = mid-1
                else:
                    print("3")
                    start = mid+1
                    
            else:
                if(target >= nums[mid] and target <= nums[end]):
                    print("4")
                    start = mid+1
                else:
                    print("5")
                    end = mid-1
                    
        return -1
            
            

#         def divide(start,end):
#             if(len(nums) == 1):
#                 if(start == end and nums[start] == target):
#                     return start
#                 else:
#                     return -1
                
#             print("start ",start,end)
#             mid = (end+start)//2
#             print("mid  ",mid," ",nums[mid])
#             if(nums[mid] == target):
#                 print("mid")
#                 return mid

# #             sorted list
#             if(nums[start] < nums[end]):
#                 if(target <= nums[mid]):
#                     print("1",nums[start:mid])
#                     return divide(start,mid-1)
#                 elif(target>=nums[mid]):
#                     print("2",nums[mid+1:end+1])
#                     return divide(mid+1,end)
                
# #             rotated list(modified binary search)
#             else:
#                 if(target <= nums[end]):
#                     print("3",nums[mid+1:end+1])
#                     return divide(mid+1,end)
#                 elif(target >= nums[start]):
#                     print("4",nums[start:mid])
#                     return divide(start,mid-1)
                
#             return -1
        
        
#         return divide(0,len(nums)-1)
            
                
            
            