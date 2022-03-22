import numpy as np


class ConnectFour:
    def __init__(self, rows, cols):
        self.board = np.zeros((rows, cols), dtype=int)

        # Player red: 1
        # Player yellow: -1
        self.move_player = 1

        # Columns A to G: 0 to 6 respectively
        self.move_column = 0

        self.drop_index = 0

        # 0: draw
        # 1: red wins
        # -1: yellow wins
        self.winner = 0

        self.WIN_SEQ = {
            1: np.full(4, 1),
            -1: np.full(4, -1)
        }

    @staticmethod
    def get_column_from_letter(letter):
        return ord(letter) - 65

    @staticmethod
    def get_player_from_colour(colour):
        return 1 if colour == 'Red' else -1

    def parse_move(self, move):
        split_move = move.split('_')
        self.move_column = self.get_column_from_letter(split_move[0])
        self.move_player = self.get_player_from_colour(split_move[1])

    def make_move(self, move):
        self.parse_move(move)
        self.drop_counter()

    def drop_counter(self):
        self.drop_index = len(self.board) - 1
        if np.any(self.board[:, self.move_column]):
            self.drop_index = np.nonzero(self.board[:, self.move_column])[0][0] - 1
        self.board[self.drop_index, self.move_column] = self.move_player

    def check_for_winning_subarray(self, main_arr):
        for i in range(len(main_arr) - 3):
            if np.array_equal(main_arr[i:i + 4], self.WIN_SEQ[self.move_player]):
                return True
        return False

    def check_below(self):
        below_region = self.board[self.drop_index:self.drop_index + 4, self.move_column]
        if len(below_region) >= 4 and np.array_equal(below_region, self.WIN_SEQ[self.move_player]):
            return True
        return False

    def check_lateral(self):
        lateral_region = self.board[self.drop_index]
        return self.check_for_winning_subarray(lateral_region)

    def check_diagonals(self):
        for i in range(len(self.board[0])):
            if self.check_for_winning_subarray(self.board.diagonal(i)) or \
                    self.check_for_winning_subarray(self.board.diagonal(-i)) or \
                    self.check_for_winning_subarray(np.fliplr(self.board).diagonal(i)) or \
                    self.check_for_winning_subarray(np.fliplr(self.board).diagonal(-i)):
                return True
        return False

    def has_winner(self):
        if self.check_below() or self.check_lateral() or self.check_diagonals():
            self.winner = self.move_player
            return True
        return False

    def get_winner(self):
        if self.winner == 1:
            return 'Red'
        elif self.winner == -1:
            return 'Yellow'
        else:
            return 'Draw'


def who_is_winner(pieces_position_list):
    game = ConnectFour(6, 7)
    for move in pieces_position_list:
        game.make_move(move)
        if game.has_winner():
            print(game.board)
            return game.get_winner()
    print(game.board)
    return game.get_winner()


print(who_is_winner([
    "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
    "D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red",
    "B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"
]))
