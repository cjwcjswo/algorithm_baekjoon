n = int(input())
result = 0
for _ in range(n):
    checker = [False for _ in range(26)]
    word = input()

    is_group_word = True
    prev_word = ''
    for w in word:
        idx = ord(w) - ord('a')
        if checker[idx] is False:
            checker[idx] = True
            prev_word = w
        else:
            if prev_word == w:
                continue
            if checker[idx] is True:
                is_group_word = False
                break
    if is_group_word:
        result += 1
print(result)