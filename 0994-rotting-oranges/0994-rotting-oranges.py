class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh_oranges = 0
        
        queue = []
        time = -1
        
        for i in grid:
            for j in i:
                if(j == 1):
                    fresh_oranges +=1 
                     
        if(fresh_oranges == 0):
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==2):
                    queue.append((i,j))
                    
        queue.append((-1,-1))            
        # print(queue)
                    
        while(queue):
            row,col = queue.pop(0)

            if(row == -1 and col== -1):
                time +=1
                if(queue):
                    queue.append((-1,-1))
            else:

                for row_off,col_off in [(0,1),(1,0),(-1,0),(0,-1)]:
                    new_row = row+row_off 
                    new_col = col+col_off

                    if(new_row in range(len(grid)) and new_col in range(len(grid[0])) and grid[new_row][new_col] == 1):
                        queue.append((new_row,new_col))
                        fresh_oranges -=1 
                        grid[new_row][new_col] = 2                    
        
                    
        return time if fresh_oranges == 0 else -1
    