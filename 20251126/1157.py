word = input()
word_count = [0 for _ in range(ord('a'), ord('z')+1)]
word_lower = word.lower()
for w in word_lower:
    word_count[ord(w)-ord('a')] += 1

max_count = 0
answer = '?'
for idx, count in enumerate(word_count):
    if count > max_count:
        max_count = count
        answer = chr(idx + ord('a')).upper()
    elif max_count != 0 and count == max_count:
        answer = '?'

print(answer)