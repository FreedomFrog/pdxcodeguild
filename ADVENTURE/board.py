class Board:
    def __init__(self):
        self.board = self.create_board()
        self.player_posx = 5
        self.player_posy = 5
        self.place_player_on_board()

    def create_board(self):
        board = [[[] for x in range(11)] for y in range(11)]
        return board

    def remove_player_icon(self):
        self.board[self.player_posy][self.player_posx] = []

    def move_player(self, let_dir):
        self.remove_player_icon()
        if let_dir == 'n':
            self.player_posy = (self.player_posy - 1) % 10
        if let_dir == 's':
            self.player_posy = (self.player_posy + 1) % 10
        if let_dir == 'w':
            self.player_posx = (self.player_posx - 1) % 10
        if let_dir == 'e':
            self.player_posx = (self.player_posx + 1) % 10
        self.place_player_on_board()

    def place_player_on_board(self):
        self.board[self.player_posy][self.player_posx].append('☺')

    def print_board(self):
        print('-' * 44)
        for line in self.board:
            print(' '.join(map(str, line)))
        print('-' * 44)


b1 = Board()
b1.print_board()
b1.move_player('n')
b1.print_board()
b1.move_player('w')
b1.print_board()

