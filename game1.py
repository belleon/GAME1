import numpy as np
def move(board,figure):
    def check(x,y):
        while 0 < x and x > 2:
            print('Error, input 0-2 x')
            x = int(input('ведите ряд хода от 0 до 2'))
        while 0 < y and y > 2:
            print('Error, input 0-2')
            y = int(input('ведите столбец хода от 0 до 2'))
        return x,y
    x,y=int(input('Введите ряд хода от 0 до 2 ')) , int(input('Введите столбец хода от 0 до 2 '))
    x,y=check(x,y)
    while board[x][y]!= b'*':
        print('Move doesnt possible')
        x, y = int(input('Введите ряд хода от 0 до 2 ')), int(input('Введите столбец хода от 0 до 2 '))
        x, y = check(x, y)
    board[x][y]=figure
def check_hor(board):
    for i in range(3):
        if board[i][1]==board[i][0]==board[i][2] and board[i][1]!=b'*':
            return f' Win {board[i][0]}'
    return False
def check_vert(board):
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i] and board[0][i]!=b'*':
           return f' Win {board[0][i]}'
    return False
def check_diag(board):
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!= b'*':
        return f' Win {board[0][0]}'
    if board[0][2]==board[1][1]==board[2][0] and board[0][2]!=b'*':
        return f' Win {board[0][0]}'
    return False
count=0
board=np.chararray((3,3))
board[:] = '*'
while count <9 or check_hor(board) or check_vert(board) or check_diag(board) :
    print(board)
    player=['X','0']
    print('Ход игрока {}'.format(player[count%2]))
    move(board,player[count%2])
    if check_hor(board) :
        print(check_hor(board))
        break
    if check_vert(board):
        print(check_vert(board))
        break
    if check_diag(board):
        print(check_diag(board))
        break
    count+=1
print(board)
if check_hor(board)==check_vert(board)==check_diag(board):
    print('Draw')
