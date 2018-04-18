def make_board():
    board = [[] for x in range(7)]
    return board


def play_move(an_int, player, curr_board):
    curr_board[an_int].append(player)
    return curr_board


def get_move():
    with open('.\connect-four-moves.txt') as f:
        text = f.read()
        split_text = text.split()
        moves = [int(move) for move in split_text]
    return moves


def print_board(curr_board):
    heightest_col = max([len(col) for col in curr_board]) - 1
    game_board_line = []
    print('- ' * 7)

    for i in range(heightest_col + 1):
        for j in range(7):
            try:

                if curr_board[j][heightest_col - i]:
                    game_board_line.append(curr_board[j][heightest_col - i])
            except IndexError:
                game_board_line.append(' ')
        game_board_line = ' '.join(game_board_line)
        print(game_board_line)
        game_board_line = []
    print('- ' * 7)


def check_horizonal(board):
    result = False
    for i in range(len(board) - 3):

        for j in range(max([len(col) for col in board]) - 1):

            try:
                a, b, c, d = board[i:i + 4][j]
                if a == b == c == d:
                    result = True
            except ValueError:
                pass
    return result


def check_vertical(board):
    result = False
    for i in range(len(board)):
        for j in range(max([len(col) - 3 for col in board])):
            try:
                a, b, c, d = board[i][j:j + 4]
                if a == b == c == d:
                    result = True
            except ValueError:
                pass
    return result


def check_diagonal(board):
    result = False
    for i in range(len(board) - 4):
        for j in range(max([len(col) for col in board])):
            try:
                if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3]:
                    result = True
            except IndexError:
                pass
            try:
                if board[i][j] == board[i - 1][j - 1] == board[i - 2][j - 2] == board[i - 3][j - 3]:
                    result = True
            except IndexError:
                pass
    return result


def check_win_cond(curr_board):
    win = False
    if check_horizonal(curr_board):
        win = True
    if check_vertical(curr_board):
        win = True
    if check_diagonal(curr_board):
        win = True
    return win


def main():
    board = make_board()
    lst_moves = get_move()
    for index, move in enumerate(lst_moves):
        if index % 2 == 0:
            player = 'R'
        else:
            player = 'Y'
        board = play_move(move - 1, player, board)
    print_board(board)
    win = check_win_cond(board)
    if win:
        print('Win condition has been met!')
    else:
        print('No winner has been determined.')


if __name__ == '__main__':
    main()
