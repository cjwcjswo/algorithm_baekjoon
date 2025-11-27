words = []
for _ in range(5):
    words.append(input())

max_len = 0
for i in range(5):
    if len(words[i]) > max_len:
        max_len = len(words[i])

result = ''
for i in range(max_len):
    for j in range(5):
        if i+1 > len(words[j]):
            continue
        result += words[j][i]

print(result)