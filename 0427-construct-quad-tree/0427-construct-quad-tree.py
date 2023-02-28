
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        
#         will check if the matrix is leaf ? O(N^2)
        def checkIsLeaf(x,y,length):
            counter = collections.defaultdict(int)
            for i in range(x,x+length):
                for j in range(y,y+length):
                    val = grid[i][j]
                    counter[val] += 1
                    
            if(len(counter) == 1):
                return True 
            else:
                return False
        
        
#         recursive function 
        def helper(x,y,length):
            
            if(checkIsLeaf(x,y,length)):
                return Node(grid[x][y],True)

            root = Node(1,False)

            offset = length//2

            root.bottomLeft = helper(x+offset,y,offset)
            root.bottomRight = helper(x+offset,y+offset,offset)
            root.topLeft = helper(x,y,offset)
            root.topRight = helper(x,y+offset,offset)
           
            return root

        return helper(0,0,len(grid))
       
                
                
                
                
                
                
                