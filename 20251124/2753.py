years_str: str = input()
years = int(years_str)
if years % 4 == 0:
    if years % 100 != 0:
        print(1)
    elif years % 400 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)