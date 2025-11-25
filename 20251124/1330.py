values: str = input()
a, b = values.split(' ')
if int(a) > int(b):
    print('>')
elif int(a) < int(b):
    print('<')
else:
    print('==')