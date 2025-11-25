arr = ['', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ', '+-=*']
sum = 0
words = input()
for word in words:
    for time, element in enumerate(arr):
        idx = element.find(word)
        if idx != -1:
            sum += time + 2
print(sum)