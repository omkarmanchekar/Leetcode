class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        N = len(board)
        
        row = [set() for _ in range(N)]
        col = [set() for _ in range(N)]
        box = [set() for _ in range(N)]
        
        
        for r in range(N):
            for c in range(N):
                
                val = board[r][c]
                
                if(val == "."):
                    continue
                    
                if(val in row[r]):
                    return False
                row[r].add(val)
                
                
                if(val in col[c]):
                    return False
                col[c].add(val)
                
                quater = (r//3) + (c//3) * 3
                if(val in box[quater]):
                    return False
                box[quater].add(val)
                
                
        return True   
                