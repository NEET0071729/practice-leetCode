'''
36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:
Input: board =[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board =[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''

def isValidSudoku(board):
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


board =[[".",".",".",".","5",".",".","1","."],
 [".","4",".","3",".",".",".",".","."],
 [".",".",".",".",".","3",".",".","1"],
 ["8",".",".",".",".",".",".","2","."],
 [".",".","2",".","7",".",".",".","."],
 [".","1","5",".",".",".",".",".","."],
 [".",".",".",".",".","2",".",".","."],
 [".","2",".","9",".",".",".",".","."],
 [".",".","4",".",".",".",".",".","."]]

'''
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board = [["9",".",".","6",".",".",".",".","."],
 [".",".",".",".","6",".",".",".","."],
 [".",".",".",".",".","1",".","3","."],
 [".",".",".",".",".",".",".",".","8"],
 [".",".",".",".",".","8",".",".","."],
 [".",".",".","4",".",".","2",".","."],
 [".",".",".",".",".",".",".",".","1"],
 ["6",".",".",".","1",".",".",".","."],
 [".",".",".",".",".",".",".",".","."]]

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
'''
print(isValidSudoku(board))