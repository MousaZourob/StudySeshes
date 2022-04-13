class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Original|  New | State
            0   |   0  |   0 
            1   |   1  |   1
            0   |   1  |   2
            1   |   0  |   3
        """
        
        ROW, COL = len(board), len(board[0])
        
        def neigh_count(x,y):
            cnt = 0
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if (i == x and j == y) or i < 0 or j < 0 or i == ROW or j == COL:
                        continue
                    if board[i][j] in [1, 3]:
                        cnt += 1
            
            return cnt
        
        for r in range(ROW):
            for c in range(COL):
                count = (neigh_count(r,c))
                if board[r][c]:
                    if count not in [2,3]:
                        board[r][c] = 3
                elif count == 3:
                    board[r][c] = 2
                    
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == 2: board[i][j] = 1 
                if board[i][j] == 3: board[i][j] = 0