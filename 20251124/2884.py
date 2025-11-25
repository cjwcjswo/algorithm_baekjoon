time: str = input()
hour, minute = time.split(' ')
hour = int(hour)
minute = int(minute)

minute -= 45
if minute < 0:
    minute = 60 + minute
    hour -= 1
if hour < 0:
    hour = 24 + hour 

print(str(hour) + " " + str(minute))