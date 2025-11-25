t = int(input())
answers = []
for _ in range(t):
    repeat, words = input().split()
    repeat = int(repeat)
    answer = ''
    for word in words:
        answer += word * repeat
    print(answer)