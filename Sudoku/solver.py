'''
Codigo tomado y adaptado de
https://techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/
'''

board = [
    [0,0,0,7,5,0,0,0,0],
    [0,3,0,0,4,8,0,2,0],
    [1,0,0,0,0,0,0,0,6],
    [0,4,0,0,0,0,0,0,8],
    [7,9,0,0,0,0,0,3,1],
    [2,0,0,0,0,0,0,7,0],
    [5,0,0,0,0,0,0,0,0],
    [0,8,0,3,2,0,0,4,0],
    [0,0,0,0,6,9,0,0,0]
]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col].append(i)

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if type(bo[i][j]) == type([]):
                return (i, j)  # row, col

    return None

def matrizdoble(board):
    doble = []
    for i in board:
        aux = []
        for j in i:
            if j == 0:
                aux.append([])
            else:
                aux.append(j)
        doble.append(aux)    
    print(doble)
    return doble

print_board(board)
matrizsub = matrizdoble(board)
print("___________________")
# print_board(matrizdoble)
solve(matrizsub)
#print_board(board)'''