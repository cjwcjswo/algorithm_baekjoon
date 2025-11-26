correct_chess_counts = [1, 1, 2, 2, 2, 8]
input_counts = list(map(int, input().split()))
for idx, input_count in enumerate(input_counts):
    print(correct_chess_counts[idx] - input_counts[idx], end=' ')