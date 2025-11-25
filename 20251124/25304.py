receipt_sum = int(input())
count = int(input())
sum = 0
for _ in range(1, count+1):
    price, num = map(int, input().split(' '))
    sum += price * num

if receipt_sum != sum:
    print("No")
else:
    print("Yes")