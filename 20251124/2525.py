hour, minute = map(int, input().split())
time = int(input())
minute += time
hour += int(minute / 60)
print(hour % 24, minute % 60)