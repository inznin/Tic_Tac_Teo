# game(XO)
# ABZUMS AI Course - Part 3 - Class Project 1
# Naznin Hoseini

# .:: step1:Initialize the Game Board 🎲 ::.

def make_board():
    board = []
    for x in range(9):
        board.append("-")
    return board

board = make_board()



# .:: step2 : display the game board ::.

def final_board (board):
    print(f"{board[0]} ⁞ {board[1]} ⁞ {board[2]}" )
    print("——+———+——")
    print(f"{board[3]} ⁞ {board[4]} ⁞ {board[5]}" )             
    print("——+———+——")
    print(f"{board[6]} ⁞ {board[7]} ⁞ {board[8]}" )            




# .:: step3 : define the players ::.

def define_players (player1):
    global player2
    if player1 == "X" :
        player2 = "O"
    elif player1 == "O":
        player2 = "X"        
    else :
        print("❌please choose onley X or O")
        return None , None

    print(f"player1 is :{player1}")
    print(f"player2 is :{player2}") 
    return player1 , player2


symbol1 , symbol2 = None , None
while symbol1 is None:
    player1 = input("player1 , please choose X or O")
    symbol1, symbol2 = define_players(player1)



# .:: step 4 : creaate a player move function ::.

def players_move (board , symbol):
    while True :
        ask1 = int(input("give me a number from 1 to 9 "))
        if ask1 in  [1,2,3,4,5,6,7,8,9]:
            index = ask1 - 1

            if board[index] == "-" :
                board[index] = symbol
                break
            else :
                print("❌ that place already taken")

        else:
            print("❌please ente a number between 1 and 9")  

            


# .::  step5 : chack for a winner  ::.

def check_winner(board,symbol):
    positions = [[0,1,2] , [3,4,5] , [6,7,8],
                 [0,3,6] , [1,4,7] , [2,5,8],
                 [2,4,6] , [0,4,8]]
    
    for pos in positions :
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == symbol :
            return True
    return False    

# .::  step6 : flip the current player  ::.

current_player = symbol1
def flip(current_player):
    if current_player == symbol1 :
        return symbol2
    else :
        return symbol1

# .::  step7 : loop untel the game end  ::.
 
move = 0
while True :
    final_board(board)
    players_move(board , current_player)
    move += 1

    if check_winner(board , current_player):
        final_board(board)
        print(f"player {current_player} wins !🎉")
        break

    if move == 9 :
        print(f"it's a tie!🤝🏼") 
        break
    
    
    current_player = flip(current_player)    










        





