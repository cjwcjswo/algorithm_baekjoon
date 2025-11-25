n, count = list(map(int, input().split()))
bucket: list[int] = [0 for _ in range(n)]

for _ in range(count):
    i, j, k = list(map(int, input().split()))
    for index in range(i-1, j):
        bucket[index] = k

for num in bucket:
    print(num, end=' ')
