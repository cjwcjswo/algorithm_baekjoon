n = int(input())

result = 2
# 2 -> 3 -> 5 -> 9 -> 17
#    1    2    4    8
# 2 + (2^n-1)
for i in range(n):
    result += pow(2, i)

print(result*result)