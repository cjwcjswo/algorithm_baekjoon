word = input()
mid = len(word) // 2
result = True
for i in range(mid):
    if word[i] != word[-(i+1)]:
        result = False
        break

print("1" if result is True else "0")