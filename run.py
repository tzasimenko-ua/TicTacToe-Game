class TicTacToe:
    def __init__(self):
        # Конструктор класу TicTacToe ініціалізує дошку як порожній список списків.
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def display_board(self):
        # Метод display_board виводить розташування клітинок та поточний стан дошки.
        print("Here's the board layout:")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        print("\nCurrent board:")
        print("\n".join([" | ".join(row) for row in self.board]))

    def check_winner(self, player):
        # Метод check_winner перевіряє, чи є переможець, перевіряючи рядки, стовпці та діагоналі.
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
        # Конструктор класу Player ініціалізує ім'я та символ гравця.
        self.name = name
        self.symbol = symbol

def print_game_rules():
    # Функція print_game_rules виводить правила гри на екран.
    print("Welcome to Tic-Tac-Toe!")
    print("Here are the rules:")
    print("1. The game is played on a 3x3 grid.")
    print("2. Players take turns placing their symbol (X or O) on an empty square.")
    print("3. The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins.")
    print("4. If all squares are filled without any player achieving a winning combination, the game is a tie.")
    print("Let's begin!")

def main():
    # Основна функція гри, керує основним процесом гри.
    print_game_rules()

    # Отримання імені та символу від гравця 1.
    player1_name = input("Player 1, enter your name: ")
    player1_symbol = input(f"{player1_name}, choose your symbol (X or O): ").upper()
    while player1_symbol not in ["X", "O"]:
        player1_symbol = input("Invalid input. Please choose X or O: ").upper()

    # Отримання імені та символу від гравця 2.
    player2_name = input("Player 2, enter your name: ")
    player2_symbol = "X" if player1_symbol == "O" else "O"
    player1 = Player(player1_name, player1_symbol)
    player2 = Player(player2_name, player2_symbol)
    game = TicTacToe()

    current_player = player1
    while True:
        # Відображення поточного стану дошки та ходу поточного гравця.
        game.display_board()
        print(f"\n{current_player.name}, it's your turn.")

        # Отримання позиції від гравця та перевірка її правильності.
        position = input("Enter position (1-9): ")
        while not position.isdigit() or int(position) not in range(1, 10) or game.board[(int(position) - 1) // 3][(int(position) - 1) % 3] != " ":
            position = input("Invalid position. Enter position (1-9): ")

        # Позначення клітинки на дошці символом поточного гравця.
        row = (int(position) - 1) // 3
        col = (int(position) - 1) % 3
        game.board[row][col] = current_player.symbol

        # Перевірка на переможця або нічию.
        if game.check_winner(current_player):
            game.display_board()
            print(f"Congratulations, {current_player.name}! You won with {current_player.symbol}s!")
            break

        if all(all(cell != " " for cell in row) for row in game.board):
            game.display_board()
            print("It's a tie!")
            break

        # Перехід до наступного гравця.
        current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    main()
