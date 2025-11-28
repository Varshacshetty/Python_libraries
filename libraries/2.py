def print_board(b):
    for r in b:
        print(' |'.join(r))


def winner(b, p):
    lines = [
        b[0], b[1], b[2],
        [b[i][0] for i in range(3)],
        [b[i][1] for i in range(3)],
        [b[i][2] for i in range(3)],
        [b[i][i] for i in range(3)],
        [b[i][2 - i] for i in range(3)]
    ]
    return [p] * 3 in lines


def full(b):
    return all(c != ' ' for r in b for c in r)


def minimax(b, maxm):
    if winner(b, 'O'):
        return 1
    if winner(b, 'X'):
        return -1
    if full(b):
        return 0

    scores = []

    for i in range(3):
        for j in range(3):
            if b[i][j] == ' ':
                b[i][j] = 'O' if maxm else 'X'
                score = minimax(b, not maxm)
                scores.append(score)
                b[i][j] = ' '

    return max(scores) if maxm else min(scores)


def best_move(b):
    best_score = -2
    move = None

    for i in range(3):
        for j in range(3):
            if b[i][j] == ' ':
                b[i][j] = 'O'
                score = minimax(b, False)
                b[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)

    return move


board = [[' '] * 3 for _ in range(3)]

while True:
    print_board(board)

    r, c = map(int, input("Your move (row col): ").split())

    if board[r][c] != ' ':
        print("Invalid!")
        continue

    board[r][c] = 'X'

    if winner(board, 'X'):
        print_board(board)
        print("You win!")
        break

    if full(board):
        print_board(board)
        print("Draw!")
        break

    m = best_move(board)

    if m:
        board[m[0]][m[1]] = 'O'
        if winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break
    else:
        print_board(board)
        print("Draw!")
        break
