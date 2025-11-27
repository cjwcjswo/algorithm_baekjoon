n, m = list(map(int, input().split()))
a = []
b = []
for _ in range(n):
    elements = list(map(int, input().split()))
    a.append(elements)

for _ in range(n):
    elements = list(map(int, input().split()))
    b.append(elements)

results = []
for m in range(len(a)):
    results.append([])
    for n in range(len(a[m])):
        results[m].append(a[m][n] + b[m][n])

for m in range(len(results)):
    print(*results[m])