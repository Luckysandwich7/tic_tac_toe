#CSE210 W02 Prove
#Ryan Alvord

def main():
    player = next_player("")
    board = create_board()
    print('Welcome to Tic Tac Toe! You will need 2 players as player 1 will be "X" and player 2 will be "O"')
    print('The rules to the game are to get 3 of your marks (X or O) in a row. When you do, YOU WIN!')
    while not (three_in_row(board) or is_a_draw(board)):
        present_board(board)
        make_move(player, board)
        player = next_player(player)
    present_board(board)
    print("You won! Thanks for playing!") 

def create_board():
    board = []
    for block in range(9):
        board.append(block + 1)
    return board

def present_board(board):
    print("\n" f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}""\n")
    
def is_a_draw(board):
    for square in range(9):
        if board[square] != "X" and board[square] != "O":
            return False
    return True 
    
def three_in_row(board):
    return (board[0] == board[1] == board[2] or
            board[0] == board[3] == board[6] or
            board[0] == board[4] == board[8] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[2] == board[4] == board[6] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8])

def make_move(player, board):
    try:
        square = int(input(f"{player}'s turn to choose a square (1-9): "))
        board[square - 1] = player
    except ValueError:
        print('Please input a number between 1-9')

def next_player(current):
    if current == "" or current == "O":
        return "X"
    elif current == "X":
        return "O"

if __name__ == "__main__":
    main()
    
