class Solution(object):
    def isValidSudoku(self, board) -> bool:
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dicto = {}
        # row and column checker
        for x in range(9):
            for y in range(9):
                if board[x][y] != '.':
                    if board[x][y] in dicto:
                        dicto[board[x][y]] += 1
                    else:
                        dicto[board[x][y]] = 1
            for z in dicto.values():
                if z > 1:
                    return False
            dicto.clear()
        for y in range(9):
            for x in range(9):
                if board[x][y] != '.':
                    if board[x][y] in dicto:
                        dicto[board[x][y]] += 1
                    else:
                        dicto[board[x][y]] = 1
            for z in dicto.values():
                if z > 1:
                    return False
            dicto.clear()
            #box checker
        for x in range(3):
            for y in range(3):
                for z in range(3*x,3*x+3):
                    if board[z][y] == '.':
                        dicto['.'] = 1
                    elif board[z][y] in dicto:
                        dicto[board[z][y]] += 1
                    else:
                        dicto[board[z][y]] = 1
            for k in dicto.values():
                if k > 1:
                    return False
            dicto.clear()
            for y in range(3, 6):
                for z in range(3*x,3*x+3):
                    if board[z][y] == '.':
                        dicto['.'] = 1
                    elif board[z][y] in dicto:
                        dicto[board[z][y]] += 1
                    else:
                        dicto[board[z][y]] = 1
            for k in dicto.values():
                if k > 1:
                    return False
            dicto.clear()
            for y in range(6,9):
                for z in range(3*x,3*x+3):
                    if board[z][y] == '.':
                        dicto['.'] = 1
                    elif board[z][y] in dicto:
                        dicto[board[z][y]] += 1
                    else:
                        dicto[board[z][y]] = 1
            for k in dicto.values():
                if k > 1:
                    return False
            dicto.clear()
        return True
    

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

s = Solution()
print(s.isValidSudoku(board))