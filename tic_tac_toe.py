# Displays the instruction for the next player
def displayInstructions():
    print('\nThis is a game of Tic-Tac-Toe.')
    print('It requires two players, and player "X" gets to go first.')
    print('Please enter in the number of the square that you want to claim.\n')

def displayBoard(board):
    # Displays the board
    print('The Board is:')
    theBoard = ''
    count = 0
    for square in board:
        theBoard += '[' + square + ']'
        count += 1
        # Keep layout based on index
        if count in [3, 6, 9]:
            theBoard += '\n'
    print(theBoard)

"""def isOpen(space):
    player_1: str = 'X'
    player_2: str = 'O'
    for space in board:
        if space == player_1 or space == player_2:
            return False
        else:
            return True"""

#Place player's mark on the board
def getMove(board, active_player):
    player_1: str = 'X'
    player_2: str = 'O'
    player_symbol = ' '
    player_up = ' '
    valid_move = False
    if active_player:
        player_up = 'Player 1'
        player_symbol = player_1
    else:
        player_up = 'Player 2'
        player_symbol = player_2
    while(not valid_move):
        chosen_square = input(player_up + ', choose a square: ')
        # Check for match
        if chosen_square in board:
            # Exception: Cannot choose a chosen square
            if chosen_square == player_1 or chosen_square == player_2:
                print('You chose poorly.')
            # Must be a valid option and can be claimed
            else:
                i = board.index(chosen_square)
                board[i] = player_symbol
                valid_move = True
        # No match, try again.
        else:
            print('You chose poorly.')

# Check if someone has won
def checkIfWin(board):
    # Rows
    win_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], \
    # Columns
    [0, 3, 6], [1, 4, 7], [2, 5, 8], \
    # Diagonals
    [0, 4, 8], [2, 4, 6]]
    for line in win_lines:
        symbol = board[line[0]]
        if symbol == board[line[1]] and symbol == board[line[2]]:
            print(symbol + ' is the winner!')
            return True
    return False

def checkDraw(board):
    player_1: str = 'X'
    player_2: str = 'O'
    for i in range(len(board)):
        # If there are spaces still available
        if (board[i] != player_1 and board[i] != player_2):
            return False
    # No spaces left  
    print('It\'s a draw! You are both found wanting.')  
    return True

def playTurn(board, player_1_go, game_over):
    getMove(board, player_1_go)
    # Check for win
    if (checkIfWin(board)):
        game_over = True        
    displayBoard(board)
    return game_over

def play_tic_tac_toe(board, player_1_go, game_over):
    displayBoard(board)
    while (not game_over):
        # Check for win
        if playTurn(board, player_1_go, game_over):
            game_over = True
            continue
        # Check for draw
        if checkDraw(board):
            game_over = True
            continue
        player_1_go = not player_1_go
    if game_over:
        new_game = input('Care to try again? Y/y for a new game. Any other character to quit.')
    if new_game.upper() == 'Y':
        new_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        new_player_1_go = True
        new_game_over = False
        play_tic_tac_toe(new_board, new_player_1_go, new_game_over)
    else:
        print('Quitter!')

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
player_1_go = True
game_over = False
displayInstructions()
play_tic_tac_toe(board, player_1_go, game_over)


player_1: str = 'X'
player_2: str = 'O'

