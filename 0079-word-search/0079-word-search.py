class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    
        start = word[0]    
        row = len(board)
        col = len(board[0])
        res = False
        
        if(len(word) > row*col):
            return False
        
        count = Counter(sum(board,[]))
        
        for letter,letterCount in Counter(word).items():
            if(count[letter] <  letterCount):
                return False
            
        
        
        dummy = [[0]*col for _ in range(row)]

        for r in range(row):
            for c in range(col):
                dummy[r][c] = board[r][c]
        
        def dfs(x,y,word,dummy,res):
            if(len(word) == 0):
                return True
            
            first = word[0]
            
            for row_off,col_off in [(0,1),(1,0),(0,-1),(-1,0)]:
                new_row = row_off + x
                new_col = col_off + y
                
                if(new_row in range(row) and new_col in range(col) and  dummy[new_row][new_col] == first):
                    dummy[new_row][new_col] = '#'
                    res = dfs(new_row,new_col,word[1:],dummy,res)
                    if(res):
                        return True 
                    dummy[new_row][new_col] = board[new_row][new_col]
            
                
                
        
        for r in range(row):
            for c in range(col):
                if(board[r][c] == start):
                    dummy[r][c] = '#'
                    res = dfs(r,c,word[1:],dummy,res)
                    dummy[r][c] = start
                    if(res == True):
                        return True 
                    
                    