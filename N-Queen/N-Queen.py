def is_under_attack(row,col):

def NQueens(row, col, n):
    while col < n:
        if not is_under_attack(row, col) == False:
            col += 1
        else:
            temp_sol.append(tuple((row, col)))
            if row == n-1:
                return True
            else:
                res=NQueens(row+1,0,n)
                if res == True:
                    return True
                else:
                    temp_sol.pop()
                    return False
    return False


n = 4
temp_sol = []
exists = NQueens()
if exists == False:
    print("Solution doesnt exists")
else:
    print("Solution is:")
    print(temp_sol)