values: str = input()
parse_values = values.split(' ')
print(sum(map(int, parse_values)))