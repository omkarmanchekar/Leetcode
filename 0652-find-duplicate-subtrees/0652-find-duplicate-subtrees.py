# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        
        def helper(root):
            
            if(not root):
                return ""
            
        
            res = ("("+ helper(root.left) +")" + str(root.val) + "("+ helper(root.right) +")" )
            
            counter[res] += 1
            if(counter[res] == 2):
                result.append(root)
            
            return res
        counter = collections.defaultdict(int)
        result = []
        
        helper(root)
        return result