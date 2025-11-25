n, m = list(map(int, input().split()))
bucket: list[int] = [num+1 for num in range(n)]
for _ in range(m):
    i, j = list(map(int, input().split()))
    bucket[i-1:j] = bucket[i-1:j][::-1]

print(*bucket)