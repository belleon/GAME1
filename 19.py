def insert_newlines(string, every=9):
    return '\n'.join(string[i:i+every] for i in range(0, len(string), every))
def check(x,y,board,coordinates):
    while y<0 or y>=9 or  x<0 or x>(len(board[::10])) or board[10*x+y]==" " or 10*x+y>len(board)-1 :
        print("Error")
        x,y=int(input("x{}=".format(coordinates))),int(input('y{}='.format(coordinates)))
    return x,y
def raw(board,l,step):
    if l+step < len(board):
        l+=step
    while l+step<len(board)-1 and (board[l] == " " or board[l]== "\n"):
        l+=step
    return l
def cond(board,l,l1):
    if l1!=l and board[l]!=' ' and board[l1]!=' 'and (board[l] == board[l1] or int(board[l])+int(board[l1])==10):
        return True
    return False
def remove_dig(board,l):
    board=board[: l]+" " + board[l + 1:]
    # board = board[: l1]+" " + board[l1 + 1:]
    return board
def add_digit(board):
    return board[:-(len(board)%10)]+ insert_newlines(board[-(len(board)%10):]+''.join([i for i in board if i!=' ' and i!='\n']))

a=[]
for i in range(1,20):
    if i != 10:
        for f in str(i):
            a.append(f)

board=insert_newlines('' .join(a))
print(board)
while len([i for i in board if i!="\n" or i!=" "])!=0:

    x=int(input("x="))
    y=int(input("y="))
    x,y=(check(x,y,board,''))
    x1=int(input("x1="))
    y1=int(input("y1="))
    x1,y1=(check(x1,y1,board,1))
    l=10*x+y
    l1=10*x1+y1
    lst =[]
    if raw(board,min(l,l1),1)== max(l,l1) or  raw(board,min(l,l1),10)== max(l,l1):
        if cond(board,l,l1)==True:
            board=remove_dig(board,l)
            board = remove_dig(board, l1)
    for i,val in enumerate(board) :
        if val!='\n' and val!=" " :
            lst.append(cond(board,i,raw(board,i,1)))
            lst.append(cond(board,i,raw(board,i,10)))
    if any(lst) == False:
        board = add_digit(board)
    print(board)




