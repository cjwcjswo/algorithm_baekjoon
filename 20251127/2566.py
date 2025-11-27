board = []
for m in range(9):
    board.append(list(map(int, input().split())))

max = -1
max_idx = [-1, -1]
for m in range(9):
    for n in range(9):
        if board[m][n] > max:
            max = board[m][n]
            max_idx[0] = m+1
            max_idx[1] = n+1

print(max)
print(*max_idx)