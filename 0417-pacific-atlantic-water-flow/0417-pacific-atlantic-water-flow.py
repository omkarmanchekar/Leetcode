class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        
        pacific = [[0] * len(heights[0]) for _ in range(len(heights))]
        atlantic = [[0] * len(heights[0]) for _ in range(len(heights))]
        
        
        pacific_queue = []
        atlantic_queue = []
        
        
        for c in range(len(heights[0])):
            pacific[0][c] = 1
            pacific_queue.append((0,c))
            
            atlantic[len(heights)-1][c] = 1
            atlantic_queue.append((len(heights)-1,c))
    
        for r in range(1,len(heights)):
            pacific[r][0] = 1
            pacific_queue.append((r,0))
            
            atlantic[len(heights)-r-1][len(heights[0])-1] = 1
            atlantic_queue.append((len(heights)-r-1,len(heights[0])-1))
            
        

        def bfs(grid,queue):
            visited = []
            while(queue):
                r,c = queue.pop(0)    
                visited.append((r,c))

                for row_off,col_off in [(0,1),(1,0),(0,-1),(-1,0)]:
                    row = r + row_off
                    col = c + col_off

                    if(row in range(len(heights)) and col in range(len(heights[0])) and grid[row][col] == 0 and (row,col) not in visited and heights[row][col] >= heights[r][c]):
                        grid[row][col] = 1
                        queue.append((row,col))

            
        bfs(pacific,pacific_queue)
        bfs(atlantic,atlantic_queue)
        
        
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if(pacific[i][j] and atlantic[i][j]):
                    res.append([i,j])
                    
        return res
            
            
            
            
       