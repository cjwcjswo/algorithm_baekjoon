n, b = list(map(int, input().split()))
result = ''

while True:
    quot = n // b
    rest = n % b

    add = ''
    if rest > 9:
        result += chr(rest - 10 + ord('a')).upper()
    else:
        result += str(rest)

    n = quot
    if quot == 0:
        break

print(result[::-1])