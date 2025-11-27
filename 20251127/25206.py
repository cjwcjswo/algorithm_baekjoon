grade_board: dict[str, float] = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0
}
sum = 0.0
credit_sum = 0.0
for _ in range(20):
    name, credit, grade = input().split()
    if grade == 'P':
        continue
    sum += float(credit) * grade_board.get(grade, 0.0)
    credit_sum += float(credit)

print(sum / credit_sum)