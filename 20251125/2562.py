max = 0
max_idx = 0
for i in range(9):
    num = int(input())
    if i == 0:
        max = num
        max_idx = i
        continue
    if num > max:
        max = num
        max_idx = i

print(max)
print(max_idx+1)

