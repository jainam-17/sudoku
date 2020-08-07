board = [
    [0,0,2,1,5,8,4,0,0],
    [0,0,0,0,0,0,0,0,0],
    [7,0,0,6,0,9,0,0,2],
    [2,0,4,0,0,0,8,0,3],
    [6,0,0,0,0,0,0,0,1],
    [1,0,9,0,0,0,5,0,7],
    [5,0,0,7,0,4,0,0,9],
    [0,0,0,0,0,0,0,0,0],
    [0,0,8,2,6,3,1,0,0]
]

#recursion -> assuming we filled the whole box
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    #Algorithm code
    for i in range(1,10):
        #try the following values
        #if valid, add them to the board
        if valid(bo,i,(row,col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    return False


def valid(bo, num, pos):
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #check col
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #check box using interger divison
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    #either gives us 0,1,2
    #box 2 multiply it by 3 to get to 6
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ") #3rd row, print horizontal row

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8: #last position and go to next line
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) #row, col
    return None

print_board(board)
solve(board)
print("________________________")
print("________________________")
print_board(board)
