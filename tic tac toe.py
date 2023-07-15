


def print_board(game):
    for row in game:
        print("|".join(row))
        print("-----")


def check_winner(game):
    
    for row in game:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
   
    for col in range(3):
        if game[0][col] == game[1][col] == game[2][col] != ' ':
            return game[0][col]
    
    if game[0][0] == game[1][1] == game[2][2] != ' ':
        return game[0][0]
    if game[0][2] == game[1][1] == game[2][0] != ' ':
        return game[0][2]
    
    return None


def play_game():
    
    game = [[' ' for _ in range(3)] for _ in range(3)]
   
    current_player = 'X'
   
    while True:
        print_board(game)
        row = int(input("Enter the row (1-3): ")) - 1
        col = int(input("Enter the column (1-3): ")) - 1

        if game[row][col] == ' ':
            game[row][col] = current_player
            winner = check_winner(game)
            if winner:
                print_board(game)
                print(f"Player {current_player} wins!")
                break
            elif all(all(cell != ' ' for cell in row) for row in game):
                print_board(game)
                print("It's a tie!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move! Try again.")


play_game()
