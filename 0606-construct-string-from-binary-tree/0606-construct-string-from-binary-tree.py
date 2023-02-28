# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = ''
        
        if(root):
            string+= str(root.val)
            
            
        if(root.left):
            string+= "("+ self.tree2str(root.left) +")"
            if(root.right):
                string += "("+ self.tree2str(root.right) +")"
        else:
#             to handle if left is null but still has right 
            if(root.right):
                string += "()("+ self.tree2str(root.right) +")"
        
        
        return string
            