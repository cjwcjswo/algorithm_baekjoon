count = int(input())
blanks = ' ' * count
stars = '*' * count

for i in range(1, count+1):
    print(f"{blanks[:count-i]}{stars[:i]}")