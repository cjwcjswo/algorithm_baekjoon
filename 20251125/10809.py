word = input()
for ascii_code in range(ord('a'), ord('z')+1):
    try:
        print(word.index(chr(ascii_code)), end=' ')
    except ValueError:
        print(-1, end=' ')