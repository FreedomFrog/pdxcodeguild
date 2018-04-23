import board
class Player:

    def __init__(self):
        self.los = 3
        self.representation = '☺'
        self.player_pos_x = 0
        self.player_pos_y = 0
        self.on_board = board.Board()

    def user_view(self):
