a, b, c = map(int, input().split())
if a == b and b == c:
    print(10000 + a * 1000)
elif a != b and b != c and c != a:
    max_value = max(a, b, c)
    print(max_value * 100)
else:
    same_value = 0
    if a == b or a == c:
        same_value = a
    elif b == c:
        same_value = b
    print(1000 + same_value * 100)