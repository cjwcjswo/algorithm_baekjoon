PREFIX = "long "
POSTFIX = "int"
STANDARD = 4

bytes = int(input())
count = bytes // STANDARD

answer = ''
for _ in range(1, count+1):
    answer += PREFIX

answer += POSTFIX
print(answer)