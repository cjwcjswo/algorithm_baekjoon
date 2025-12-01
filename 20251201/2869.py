a, b, v = list(map(int, input().split()))
if a >= v:
    print(1)
else:
    predict = (v - a) // (a - b)
    print(predict + 1 + (0 if (v - a) % (a - b) == 0 else 1))