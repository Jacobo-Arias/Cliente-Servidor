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




def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if type(bo[i][j]) is int:
                show = bo[i][j]
            else:
                show = 0 
            if j == 8:
                print(show)
            else:
                print(str(show) + " ", end="")

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
    return doble

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

def filtrar(matrizsub):
    for fil in range(len(matrizsub)):
        for col in range(len(matrizsub)):
            for num in range(1,10):
                if valid(matrizsub,num,(fil,col)) and type(matrizsub[fil][col]) is list:
                    matrizsub[fil][col].append(num)
    return matrizsub


def fillone(matrizsub):
    for fil in range(len(matrizsub)):
        for col in range(len(matrizsub)):
            if type(matrizsub[fil][col]) is list:
                if len(matrizsub[fil][col]) == 1:
                    matrizsub[fil][col] = matrizsub[fil][col].pop()
    return matrizsub

def reset(matrizsub):
    for fil in range(len(matrizsub)):
        for col in range(len(matrizsub)):
            if type(matrizsub[fil][col]) is list:
                matrizsub[fil][col] = []
    return matrizsub

def work(matrizsub):
    matrizsub = filtrar(matrizsub)
    matrizsub = fillone(matrizsub)
    matrizsub = reset(matrizsub)
    return matrizsub

print_board(board)
print('-----------------------------------')
matrizsub = matrizdoble(board)
matrizsub = work(matrizsub)
matrizsub = work(matrizsub)
print_board(matrizsub)

        

