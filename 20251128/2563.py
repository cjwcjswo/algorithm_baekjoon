grid = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())
for _ in range(n):
    x, y = list(map(int, input().split()))
    for i in range(10):
        for j in range(10):
            grid[x+i][y+j] += 1

sum = 100 * 100
for row in grid:
    for column in row:
        if column == 0:
            sum -= 1

print(sum) 
