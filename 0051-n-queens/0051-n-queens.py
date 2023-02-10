class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def helper(path):
            res = []
            
            for i in path:
                s = '.' * (len(path)-1)
                s = s[:path[i]] + 'Q' + s[path[i]:]
                res.append(s)
                
            return res
        
        
        def backtracking(row,col,diagonal,antidiagonal,tracking,res):
            if(row == n):
                res.append(helper(tracking))
                # print(res)
                return 
            
            
            for c in range(n):
                dia = row-c
                antidia = row+c
                if(c in col or dia in diagonal or antidia in antidiagonal):
                    continue
                
                col.add(c)
                diagonal.add(dia)
                antidiagonal.add(antidia)
                tracking[row] = c
                
                backtracking(row+1,col,diagonal,antidiagonal,tracking,res)
                
                col.remove(c)
                diagonal.remove(dia)
                antidiagonal.remove(antidia)
                tracking.pop(row)
                
            
            return res
                
            
        
        
        
        res = []
        backtracking(0,set(),set(),set(),collections.defaultdict(),res)
        return res