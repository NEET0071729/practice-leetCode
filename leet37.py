import numpy as np
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead
        """
        arr = np.array(board, dtype='<U1')
        solution(arr)
        board[:] = arr.tolist()
    
def solution(board):
    find = findempty(board)
    
    if not find:
        return True
    
    filler = ['1','2','3','4','5','6','7','8','9']
    for num in filler:
        if is_valid(num, find[0], find[1], board):
            board[find[0] ,find[1]] = num
            if solution(board):
                return True
            board[find[0], find[1]] = '.'
    return False

#find empty
def findempty(board):
    if '.' in board:
        b = np.nonzero(board == '.')
        return (int(b[0][0]) , int(b[1][0]))
    return None

#validation
def is_valid(num, rows, column, board):
    #check column and column
    if num in board[:, column] or num in board[rows,:] or num in board[3*(rows//3):3*(rows//3)+3, 3*(column//3): 3*(column//3)+3]:
        return False
    return True

board = [["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]]

s = Solution()
s.solveSudoku(board)
print(board)