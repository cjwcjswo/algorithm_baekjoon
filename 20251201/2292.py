#   2, 8, 20, 38 // 1, 6, 12, 18
#    7, 19, 37
n = int(input())
if n == 1:
    print(1)
else:
    count = 1
    while True:
        min = (3 * count ** 2) - (3 * count) + 2

        if min <= n and n <= min + count * 6 - 1:
            break
        
        count += 1
    print(count + 1)