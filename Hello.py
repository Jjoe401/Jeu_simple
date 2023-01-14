import random
class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # initiation rang
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # initiation colonne
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # initiation  des diagonales
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"le tour du joueur {player} ")

            self.show_board()

            # pour le joueur1
            row, col = list(
                map(int, input("Entrer la ligne et colonne: ").split()))
            print()

            # initie le resultat
            self.fix_spot(row - 1, col - 1, player)

            # voir sy je joueur a gagné
            if self.is_player_win(player):
                print(f" hip hip Le joueur {player} à gagné houra")
                break

            # avoir un égalité d  n le jeu
            if self.is_board_filled():
                print(" Wauoh Egalité!")
                break

            # echange de tour
            player = self.swap_player_turn(player)

        # le tableau final
        print()
        self.show_board()


# commencement du jeu
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
