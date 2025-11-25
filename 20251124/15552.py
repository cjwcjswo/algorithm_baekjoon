import sys

test_count = int(sys.stdin.readline().rstrip())

for _ in range(1, test_count+1):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    print(a+b)