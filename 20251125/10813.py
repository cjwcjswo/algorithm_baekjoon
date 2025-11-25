n, m = list(map(int, input().split()))
bucket = [num+1 for num in range(n)]
for _ in range(m):
    i, j = list(map(int, input().split()))
    temp = bucket[i-1]
    bucket[i-1] = bucket[j-1]
    bucket[j-1] = temp
print(*bucket)