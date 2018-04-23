

# class Board:
#     def __init__(self, player_obj=player.Player):
#         self.board = self.create_board()
#         self.player_posx = 5
#         self.player_posy = 5
#         self.place_player_on_board(player_obj)
#
#     def create_board(self):
#         board = [[[] for x in range(self.player_obj.los * 2 + 1)] for y in range(self.player_obj.los * 2 + 1)]
#         return board
#
#     def remove_player_icon(self):
#         self.board[self.player_posy][self.player_posx] = []
#
#     def move_player(self, let_dir):
#
#         self.remove_player_icon()
#         if let_dir == 'n':
#             self.player_posy = (self.player_posy - 1) % 10
#         if let_dir == 's':
#             self.player_posy = (self.player_posy + 1) % 10
#         if let_dir == 'w':
#             self.player_posx = (self.player_posx - 1) % 10
#         if let_dir == 'e':
#             self.player_posx = (self.player_posx + 1) % 10
#         self.place_player_on_board()
#
#     def place_player_on_board(self):
#         self.board[self.player_posy][self.player_posx].append('☺')
#
#     def print_board(self):
#         print('-' * 44)
#         for line in self.board:
#             print(' '.join(map(str, line)))
#         print('-' * 44)
#
#
# b1 = Board()
# b1.print_board()
# b1.move_player('n')
# b1.print_board()
# b1.move_player('w')
# b1.print_board()

class Board:
    def __init__(self):
        self.height = 10
        self.weidth = 10
        self.play_area = self.make_board()

    def make_board(self):
        play_area = [[[] for x in range(self.height)] for y in range(self.weidth)]
        return play_area



g1 = Board()
print(g1.play_area)