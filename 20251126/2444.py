n = int(input())
for idx in range(2*n-1):
    stars = ''
    spaces = ''
    if idx + 1 <= n:
        stars = '*' * (2 * idx + 1)
        spaces = ' ' * (n - (idx+1))
    else:
        stars = '*' * (4 * n - 2 * idx - 3)
        spaces = ' ' * ((idx+1) - n)
    print(f'{spaces}{stars}')
                