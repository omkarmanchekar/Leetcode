class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead
        """
        
        def helper(new_row,new_col,rooms,visited):
            if(new_row in range(len(rooms)) and new_col in range(len(rooms[0])) and rooms[new_row][new_col] >0 and rooms[new_row][new_col] <= 2147483647 and ((new_row,new_col) not in visited)):
                return True
            else:
                return False
        
        def bfs(r,c,rooms):
            queue = [(r,c,0)]
            visited = [(r,c)]
            
            while(queue):
                row,col,distance = queue.pop(0)
                
                for row_off,col_off in [(0,1),(1,0),(-1,0),(0,-1)]:
                    new_row = row+row_off
                    new_col = col+ col_off
                    # if(helper(new_row,new_col,rooms,visited)):
                    #         queue.append((new_row,new_col,distance + 1))
                    #         rooms[new_row][new_col] = min(distance + 1,rooms[new_row][new_col])
                    #         visited.append((new_row,new_col))
                    
                    if(helper(new_row,new_col,rooms,visited)):
                        if(rooms[new_row][new_col] > distance + 1):
                            queue.append((new_row,new_col,distance + 1))
                            rooms[new_row][new_col] = min(distance + 1,rooms[new_row][new_col])
                            visited.append((new_row,new_col))
                            
                            
        
                        
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if(rooms[i][j] == 0):
                        bfs(i,j,rooms)


                       
        