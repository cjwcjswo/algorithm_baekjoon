num = int(input())
answers = []
for i in range(num):
    a, b = map(int, input().split())
    answers.append(a+b)

for answer in answers:
    print(answer)