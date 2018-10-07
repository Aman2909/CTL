''''4x4 Sudoku'''
import math


def Sudoku(pos, num, n):
    while num <= n:
        row = pos_list[pos][0]
        col = pos_list[pos][1]
        if is_possible(row, col, num) == False:
            num += 1
        else:
            S[row][col] = num
            if pos == (len(pos_list) - 1):
                return True
            else:
                res = Sudoku(pos + 1, 1, n)
                if res == True:
                    return True
                else:
                    S[row][col] = None
                    num += 1
    return False

def is_possible(row, col, num):
    row_q = row // int(math.sqrt(n))
    col_q = col // int(math.sqrt(n))
    for i in range(n):
        if S[row][i] == num:
            # print("row")
            return False
        if S[i][col] == num:
            # print("col")
            return False

    # x = row_q * rootn
    # y = col_q * rootn
    # for i in range(x, x + rootn):
    #     for j in range(y, y + rootn):
    #         if S[i][j] == num:
    #             # print("box")
    #             return False

    return True


S = [[None, None, None, 2],
     [None, 1, None, None],
     [None, None, None, None],
     [None, None, 4, None]]
pos_list = []
n = 4
rootn = int(math.sqrt(n))
for i in range(n):
    for j in range(n):
        if S[i][j] == None:
            pos_list.append(tuple((i, j)))
Sudoku(0, 1, n)
print(S)
