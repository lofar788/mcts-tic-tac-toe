import numpy as np


class Board:

    def __init__(self):
        self.board = np.zeros(9)
        self.player = 0

    def is_space_empty(self, index):
        return self.board[index] == 0

    def player_move(self, player, index):
        if self.is_space_empty(index):
            self.board[index] = player
            return True
        else:
            print('space is taken!')
            return False

    def get_space_name(self, index):
        if self.board[index] == 0:
            return ' '
        elif self.board[index] == 1:
            return 'O'
        elif self.board[index] == 2:
            return 'X'

    def check_winner(self, player):
        # check horizontal
        if self.board[6] == player and self.board[7] == player and self.board[8] == player:
            return True
        elif self.board[3] == player and self.board[4] == player and self.board[5] == player:
            return True
        elif self.board[0] == player and self.board[1] == player and self.board[2] == player:
            return True
        # check diagonal
        elif self.board[0] == player and self.board[4] == player and self.board[8] == player:
            return True
        elif self.board[2] == player and self.board[4] == player and self.board[6] == player:
            return True
        # check verticle
        elif self.board[0] == player and self.board[3] == player and self.board[6] == player:
            return True
        elif self.board[1] == player and self.board[4] == player and self.board[7] == player:
            return True
        elif self.board[2] == player and self.board[5] == player and self.board[8] == player:
            return True
        else:
            return False

    def check_if_draw(self):
        draw = True
        for i in range(9):
            if self.board[i]==0:
                draw = False
                break
        return draw

    def clear_board(self):
        self.board = np.zeros(9)

    def available_actions(self):
        actions = []
        for i in range(9):
            if self.board[i] == 0:
                actions.append(i)
        return actions

    def print_board(self):
        print('{}|{}|{}'.format(self.get_space_name(6), self.get_space_name(7), self.get_space_name(8)))
        print('------')
        print('{}|{}|{}'.format(self.get_space_name(3), self.get_space_name(4), self.get_space_name(5)))
        print('------')
        print('{}|{}|{}'.format(self.get_space_name(0), self.get_space_name(1), self.get_space_name(2)))


def play_game(player):
    while True:
        player += 1
        available_actions = board.available_actions(board.board)
        if available_actions:
            print('available moves are {}'.format(str(available_actions.values())))
            while True:
                move = input('player {} move!'.format(player))
                try:
                    if int(move) in available_actions.values():
                        board.player_move(player, int(move))
                        break
                    else:
                        print('not a legal move')
                except ValueError:
                    print('not a number')
            if board.check_winner(player):
                print('player {} is the winner'.format(player))
                break
            else:
                board.print_board()
            player %= 2
        else:
            print('draw')
            break


if __name__ == '__main__':
    player = 0
    board = Board()
    board.print_board()
    play_game(player)
