class TicTacToe:
    def __init__(self):
        # Constructor of the TicTacToe class initializes the board as an empty list of lists.
        self.board = [[" " for _ in range(3)] for _ in range(3)]

def display_board(self):
        # The display_board method prints the cell positions and the current state of the board.
        print("Here's the board layout:")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        print("\nCurrent board:")
        print("\n".join([" | ".join(row) for row in self.board]))

def check_winner(self, player):
    # The check_winner method checks for a winner by examining rows, columns, and diagonals.

        for row in self.board:
            if all(cell == player.symbol for cell in row):
                return True

        for col in range(3):
            if all(self.board[row][col] == player.symbol for row in range(3)):
                return True

        if all(self.board[i][i] == player.symbol for i in range(3)):
            return True

        if all(self.board[i][2 - i] == player.symbol for i in range(3)):
            return True

        return False

class Player:
    def __init__(self, name, symbol):
        # Constructor of the Player class initializes the name and symbol of the player.
        self.name = name
        self.symbol = symbol

def print_game_rules():
    # The print_game_rules function prints the game rules to the screen.
    print("Welcome to Tic-Tac-Toe!")
    print("Here are the rules:")
    print("1. The game is played on a 3x3 grid.")
    print("2. Players take turns placing their symbol (X or O) on an empty square.")
    print("3. The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins.")
    print("4. If all squares are filled without any player achieving a winning combination, the game is a tie.")
    print("Let's begin!")        