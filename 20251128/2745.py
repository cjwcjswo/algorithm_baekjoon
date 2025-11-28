n, b = input().split()

sum = 0
n_len = len(n)
for idx, word in enumerate(n):
    square = pow(int(b), n_len - idx - 1)
    if word.isdigit():
        sum +=  square * int(word)
    else:
        sum += square * (9 + (ord(word.lower()) - ord('a') + 1))
print(sum)