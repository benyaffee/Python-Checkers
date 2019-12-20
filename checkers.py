#Checkers
def intro():
    print("Welcome to Checkers!!!")
    print("Player 1, you're x's. Player 2, you're o's")

winner = "None"

board = [['~','x','~','x','~','x','~','x'],
['x','~','x','~','x','~','x','~'],
['~','x','~','x','~','x','~','x'],
['_','~','_','~','_','~','_','~'],
['~','_','~','_','~','_','~','_'],
['o','~','o','~','o','~','o','~'],
['~','o','~','o','~','o','~','o'],
['o','~','o','~','o','~','o','~']]

def print_board(current_board):
    #print("{'0'}{'1'}{'2'}{'3'}{'4'}")
    x = 0
    print("    0 1 2 3 4 5 6 7 \n")

    for row in range(0,len(current_board)):
        print(x," ", end = ' ')
        x += 1
        for column in range(0, len(current_board[row])):
            print(board[row][column],end = ' ')
            if column == 7:
                print('\n')

def choose_piece(player, marker, king_marker):
    print("Your move, ", "Player", player)
    move = 'no'
    while move == 'no':
        print("Select a piece using the coordinates")
        col = int(input("Choose a column: "))
        row = int(input("Choose a row: "))
        if board[row][col] == marker:
            move_piece(row, col, player, marker, 'pawn')
            move = 'yes'
        elif board[row][col] == king_marker:
            move_piece(row, col, player, king_marker, 'king')
            move = 'yes'
        else:
            print("You don't have a piece there. Remember, Player 1 has x's and Player 2 has o's")
#Immovable piece
            
def multijump(y,x,jumps,rank):
    i=0
    
    for i in range(0,jumps):
        
        print("Select the coordinates for jump #",i+1,": ")
        col = int(input("Choose a column: "))
        row = int(input("Choose a row: "))
        if (row>7 or row<0) or (col>7 or col<0):
            move='no'
        else:
            if rank=="pawn":
                if col == x+2 and row == y+2 and (board[y+1][x+1]=="o" or board[y+1][x+1]=="O"):
                    board[row][col] = "x"
                    board[y+1][x+1]="_"
                    board[y][x]="_"
                    x+=2
                    y+=2
                    move='yes'
                elif col == x-2 and row == y+2 and (board[y+1][x-1]=="o" or board[y+1][x-1]=="O"):
                    board[row][col] = "x"
                    board[y+1][x-1]="_"
                    board[y][x]="_"
                    x-=2
                    y+=2
                    move='yes'
                elif col == x+2 and row == y-2 and (board[y-1][x+1]=="x" or board[y-1][x+1]=="X"):
                    board[row][col]= "o"
                    board[y-1][x+1]= "_"
                    board[y][x]="_"
                    x+=2
                    y-=2
                    move='yes'
                elif col == x-2 and row == y-2 and (board[y-1][x-1]=="x" or board[y-1][x-1]=="X"):
                    board[row][col] = "o"
                    board[y-1][x-1]="_"
                    board[y][x]="_"
                    x-=2
                    y-=2
                    move='yes'
                else:
                    print("Move not allowed")
                    i-=1
                    move='no'
            if rank=="king":
                if col == x+2 and row == y+2 and (board[y+1][x+1]=="o" or board[y+1][x+1]=="O"):
                    board[row][col] = "X"
                    board[y+1][x+1]="_"
                    board[y][x]="_"
                    x+=2
                    y+=2
                    move='yes'
                elif col == x-2 and row == y+2 and (board[y+1][x-1]=="o" or board[y+1][x-1]=="O"):
                    board[row][col] = "X"
                    board[y+1][x-1]="_"
                    board[y][x]="_"
                    x-=2
                    y+=2
                    move='yes'
                elif col == x+2 and row == y-2 and (board[y-1][x+1]=="o" or board[y-1][x+1]=="O"):
                    board[row][col]= "X"
                    board[y-1][x+1]= "_"
                    board[y][x]="_"
                    x+=2
                    y-=2
                    move='yes'
                elif col == x-2 and row == y-2 and (board[y-1][x-1]=="o" or board[y-1][x-1]=="O"):
                    board[row][col] = "X"
                    board[y-1][x-1]="_"
                    board[y][x]="_"
                    x-=2
                    y-=2
                    move = 'yes'
                elif col == x+2 and row == y+2 and (board[y+1][x+1]=="x" or board[y+1][x+1]=="X"):
                    board[row][col] = "O"
                    board[y+1][x+1]="_"
                    board[y][x]="_"
                    x+=2
                    y+=2
                    move = 'yes'
                elif col == x-2 and row == y+2 and (board[y+1][x-1]=="x" or board[y+1][x-1]=="X"):
                    board[row][col] = "O"
                    board[y+1][x-1]="_"
                    board[y][x]="_"
                    x-=2
                    y+=2
                    move ='yes'
                elif col == x+2 and row == y-2 and (board[y-1][x+1]=="x" or board[y-1][x+1]=="X"):
                    board[row][col]= "O"
                    board[y-1][x+1]= "_"
                    board[y][x]="_"
                    x+=2
                    y-=2
                    move = 'yes'
                elif col == x-2 and row == y-2 and (board[y-1][x-1]=="x" or board[y-1][x-1]=="X"):
                    board[row][col] = "O"
                    board[y-1][x-1]="_"
                    board[y][x]="_"
                    x-=2
                    y-=2
                    move = 'yes'
                else:
                    print("Move not allowed")
                    i-=1
                    move = 'no'
        i+=1
    return move
    #return multi_coord[row][col]
        
#def move_type():
    #print("Move types:")
    #print("1: No Jump")
    #print("2: Jump")
    #move = int(input("Choose a move type: "))
    #if move == 1:
     #move_piece()
    #elif move == 2:
            #jump_move
    #else:
            #improper imput

def move_piece(y , x, player, marker, rank):
    move = 'no'
    while move == 'no':
        
        jumps = int(input("How many pieces would you like to jump (0, 1, 2, 3, etc.)? "))
        if jumps > 1:
            brk=multijump(y,x,jumps,rank)
            if brk == 'yes':
                break
            else:
                print("Invalid coordinates.")

        if jumps == 0:
            print("Select the coordinates where you want your piece to go: ")
            col = int(input("Choose a column: "))
            row = int(input("Choose a row: "))

        
            if rank == 'pawn':
                
                if board[row][col] == '_':
                    
                    if marker == "x":
                        
                        if (col == x+1 and row == y+1) or (col == x-1 and row == y+1):
                            board[row][col] = "x"
                            move = 'yes'
                            
                        else:
                            print("Move not allowed")
                    elif marker == "o":
    
                        if (col == x+1 and row == y-1) or (col == x-1 and row == y-1):
                            board[row][col] = "o"
                            move = 'yes'
                        else:
                            print("Move not allowed")
                else:
                    print("Space Occupied")            
            elif rank == 'king':
                if board[row][col] == '_':
                    
                    if marker == "X":
                        
                        if (col == x+1 and row == y+1) or (col == x-1 and row == y+1) or (col == x+1 and row == y-1) or (col == x-1 and row == y-1):
                            board[row][col] = "X"
                            move = 'yes'
                            
                        else:
                            print("Move not allowed")
                    elif marker == "O":
    
                        if (col == x+1 and row == y+1) or (col == x-1 and row == y+1) or (col == x+1 and row == y-1) or (col == x-1 and row == y-1):
                            board[row][col] = "O"
                            move = 'yes'
                        else:
                            print("Move not allowed")
                else:
                    print("Space Occupied")
            else:
                print("Strange piece")

        if jumps == 1:
            print("Select the coordinates where you want your piece to go: ")
            col = int(input("Choose a column: "))
            row = int(input("Choose a row: "))

        
            if rank == 'pawn':
                
                if board[row][col] == '_':
                    
                    if marker == "x":
                        
                        if col == x+2 and row == y+2 and (board[y+1][x+1]=="o" or board[y+1][x+1]=="O"):
                            board[row][col] = "x"
                            board[y+1][x+1]="_"
                            move = 'yes'

                        elif col == x-2 and row == y+2 and (board[y+1][x-1]=="o" or board[y+1][x-1]=="O"):
                            board[row][col] = "x"
                            board[y+1][x-1]="_"
                            move = 'yes'
                        else:
                            print("Move not allowed")
                    elif marker == "o":
    
                        if col == x+2 and row == y-2 and (board[y-1][x+1]=="x" or board[y-1][x+1]=="X"):
                            board[row][col]= "o"
                            board[y-1][x+1]= "_"
                            move = 'yes'
                        elif col == x-2 and row == y-2 and (board[y-1][x-1]=="x" or board[y-1][x-1]=="X"):
                            board[row][col] = "o"
                            board[y-1][x-1]="_"
                            move = 'yes'
                        else:
                            print("Move not allowed")
                else:
                    print("Space Occupied")
                    
            elif rank == 'king':
                if board[row][col] == '_':
                    
                    if marker == "x":
                        
                        if col == x+2 and row == y+2 and (board[y+1][x+1]=="o" or board[y+1][x+1]=="O"):
                            board[row][col] = "x"
                            board[y+1][x+1]="_"
                            move = 'yes'

                        elif col == x-2 and row == y+2 and (board[y+1][x-1]=="o" or board[y+1][x-1]=="O"):
                            board[row][col] = "x"
                            board[y+1][x-1]="_"
                            move = 'yes'
                        elif col == x+2 and row == y-2 and (board[y-1][x+1]=="o" or board[y-1][x+1]=="O"):
                            board[row][col]= "x"
                            board[y-1][x+1]= "_"
                            move = 'yes'
                        elif col == x-2 and row == y-2 and (board[y-1][x-1]=="o" or board[y-1][x-1]=="O"):
                            board[row][col] = "x"
                            board[y-1][x-1]="_"
                            move = 'yes'
                        else:
                            print("Move not allowed")
                    elif marker == "o":
    
                        if col == x+2 and row == y-2 and (board[y-1][x+1]=="x" or board[y-1][x+1]=="X"):
                            board[row][col]= "o"
                            board[y-1][x+1]= "_"
                            move = 'yes'
                        elif col == x-2 and row == y-2 and (board[y-1][x-1]=="x" or board[y-1][x-1]=="X"):
                            board[row][col] = "o"
                            board[y-1][x-1]="_"
                            move = 'yes'
                        elif col == x+2 and row == y+2 and (board[y+1][x+1]=="x" or board[y+1][x+1]=="X"):
                            board[row][col] = "x"
                            board[y+1][x+1]="_"
                            move = 'yes'

                        elif col == x-2 and row == y+2 and (board[y+1][x-1]=="x" or board[y+1][x-1]=="X"):
                            board[row][col] = "x"
                            board[y+1][x-1]="_"
                            move = 'yes'
                        else:
                            print("Move not allowed")
                else:
                    print("Space Occupied")
            else:
                print("Strange piece")

        
    board[y][x] = "_"
    '''if jumps < 2:
        coord ={'col':col, 'row':row}
        print('col =', coord['col'],"and row =", coord['row'])
        return coord
    else:
        coord = {'col':multi_coord['col'], 'row': multi_coord['row']}
        return coord
'''
def king_me(marker):
    '''if marker == "x" and coord['row'] == 7:
        board[coord['row']][coord['col']] = "X"
     elif marker == "o" and coord['row'] == 0:
        board[coord['row']][coord['col']] = "O"
    '''
    print("Looking for king...")
    if marker == "o":
        print('Marker is o')
        i=1
        for i in range(1,8):
            print(board[0][i])
            if board[0][i] == marker:
                board[0][i] = "O"
                i+2
    elif marker == "x":
        print('Marker is x')
        i=0
        for i in range(0,7):
            print(board[7][i])
            if board[7][i]==marker:
                board[7][i] = "X"
    else:
        print("Nope, marker = ", marker)
    
def check_winner(current_board):
    x = 0
    o = 0
    for row in range(0,len(current_board)):
        for column in range(0, len(current_board[row])):
            if current_board[row][column] == 'x':
                x += 1
            elif current_board[row][column] == 'o':
                o += 1
    if x == 0:
        winner == "Player 2"
    elif o == 0:
        winner == "Player 1"

def main():
    intro()
    
    while winner == "None":
        print_board(board)
        choose_piece(1, 'x','X')
        #print(pos_x['row'])
        king_me('x')
        print_board(board)
        choose_piece(2,'o', 'O')
        king_me('o')
        check_winner(board)
main()
