# 1, 2~3, 4~6, 7~10, 11~15
x = int(input())

if x == 1:
    print("1/1")
else:
    n, m = 0, 0
    count = 1
    while True:
        n = 1 + int((0.5 * (count ** 2 + count)))
        m = n + count
        if n <= x and x <= m:
            break
        count += 1


    if count % 2 == 0:
        print(f"{count+1 - (x-n)}/{1 + x-n}")
    else:
        print(f"{1 + x-n}/{count+1 - (x-n)}")