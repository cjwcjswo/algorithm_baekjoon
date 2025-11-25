checks: list[bool] = [False for _ in range(30)]
for _ in range(28):
    checks[int(input())-1] = True
for idx, check in enumerate(checks):
    if check is False:
        print(idx+1)