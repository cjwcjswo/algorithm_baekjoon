t = int(input())
credit = [25, 10, 5, 1]
for _ in range(t):
    total = int(input())

    for c in credit:
        print(total // c, end=' ')
        total = total % c