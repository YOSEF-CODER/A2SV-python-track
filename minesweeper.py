from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        def inbound(row, col):
            return (0 <= row < len(board) and 0 <= col < len(board[0]))

        def dfs(row, col):
          
            if board[row][col] == 'M':
                board[row][col] = 'X'
                return 
            

         
            if board[row][col] != 'E':
                return

            mine_count = 0
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                

                if inbound(new_row, new_col) and board[new_row][new_col] in ['X', 'M']:
                    mine_count += 1

         
            if mine_count > 0:
                board[row][col] = str(mine_count)
          
            else:
                board[row][col] = 'B'

                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    

                    if inbound(new_row, new_col):
                        dfs(new_row, new_col)
        
        dfs(click[0], click[1])
        return board