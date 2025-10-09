import math

# The Tic-Tac-Toe board is represented as a list of 9 elements.
# '-' represents an empty cell.
board = ['-'] * 9
human_player = 'O'
ai_player = 'X'

def print_board(current_board):
    """Prints the Tic-Tac-Toe board in a 3x3 grid."""
    print("-------------")
    for i in range(3):
        print(f"| {current_board[i*3]} | {current_board[i*3+1]} | {current_board[i*3+2]} |")
        print("-------------")

def is_winner(b, player):
    """Checks if the given player has won the game."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if b[condition[0]] == b[condition[1]] == b[condition[2]] == player:
            return True
    return False

def check_game_over(b):
    """Checks for a terminal state (win, loss, or draw) and returns a utility score."""
    if is_winner(b, ai_player):
        return 1  # AI wins
    elif is_winner(b, human_player):
        return -1 # Human wins
    elif '-' not in b: # Board is full
        return 0  # Draw
    else:
        return None # Game is not over

def minimax(b, is_maximizing):
    """Minimax algorithm implementation to determine the score of a board state."""
    score = check_game_over(b)
    if score is not None:
        return score

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == '-':
                b[i] = ai_player
                score = minimax(b, False)
                b[i] = '-'
                best_score = max(score, best_score)
        return best_score
    else: # Minimizing player
        best_score = math.inf
        for i in range(9):
            if b[i] == '-':
                b[i] = human_player
                score = minimax(b, True)
                b[i] = '-'
                best_score = min(score, best_score)
        return best_score

def find_best_move(b):
    """Finds the best possible move for the AI by iterating through all empty cells."""
    best_score = -math.inf
    move = -1
    for i in range(9):
        if b[i] == '-':
            b[i] = ai_player
            score = minimax(b, False)
            b[i] = '-'
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game loop
if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O'. The AI is 'X'. Cell numbers are 0-8.")
    print_board(board)

    while True:
        # Human's turn
        try:
            player_move = int(input("Enter your move (0-8): "))
            if 0 <= player_move <= 8 and board[player_move] == '-':
                board[player_move] = human_player
            else:
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        print("\nYour move:")
        print_board(board)

        if check_game_over(board) is not None:
            break

        # AI's turn
        print("\nAI is thinking...")
        ai_move = find_best_move(board)
        board[ai_move] = ai_player
        
        print(f"AI chose position {ai_move}:")
        print_board(board)

        if check_game_over(board) is not None:
            break

    # Announce the result
    result = check_game_over(board)
    if result == 1:
        print("AI wins! Better luck next time. 😉")
    elif result == -1:
        print("Congratulations! You win! 🏆")
    else:
        print("It's a draw! 🤝")



