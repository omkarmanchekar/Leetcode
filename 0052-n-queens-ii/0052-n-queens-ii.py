class Solution:
    def totalNQueens(self, n: int) -> int:

# You can place one queen at each row 
#  For each row check if the place is safe by checking col, diagonal, anti diagonal 
#  col is easy to keep track of 
#  Diagonal - for each square (row-col) value will be same for each diagonal 
#  Anti Diagonal - for each square (row+col) value will be same for each anti diagonal

        def helper(row,col,diagonal,antiDiagonal):
            
            if(row == n):
                return 1
            
            res = 0
            for c in range(n):
                dia = row-c
                anti_dia = row+c
                
                if(c in col or dia in diagonal or anti_dia in antiDiagonal):
                    continue 
                    
                col.add(c)
                diagonal.add(dia)
                antiDiagonal.add(anti_dia)
                
                res += helper(row+1,col,diagonal,antiDiagonal)
                
                col.remove(c)
                diagonal.remove(dia)
                antiDiagonal.remove(anti_dia)
                
            return res
            
        return helper(0,set(),set(),set())
        