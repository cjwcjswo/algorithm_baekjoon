# 2025년 11월 27일 문제 풀이 정리

## 📚 학습 내용 요약

### 1. 2차원 배열(행렬) 처리

#### 문제: 10798 (세로로 읽기), 2566 (최댓값), 2738 (행렬 덧셈)
- **핵심 문법**: 2차원 리스트, 중첩 반복문, 인덱싱
- **학습 포인트**:
  - 2차원 리스트 생성 및 접근
  - 행과 열의 인덱스 처리
  - 행렬 연산 (덧셈, 최댓값 찾기)

**개선된 코드 예시**:
```python
# 10798번 - 세로로 읽기 (더 간결한 버전)
words = [input() for _ in range(5)]
max_len = max(len(word) for word in words)
result = ''
for i in range(max_len):
    for word in words:
        if i < len(word):
            result += word[i]
print(result)

# 2566번 - 최댓값 찾기 (enumerate 활용)
board = [list(map(int, input().split())) for _ in range(9)]
max_value = -1
max_row, max_col = 0, 0
for i, row in enumerate(board):
    for j, value in enumerate(row):
        if value > max_value:
            max_value = value
            max_row, max_col = i + 1, j + 1
print(max_value)
print(max_row, max_col)

# 2738번 - 행렬 덧셈 (리스트 컴프리헨션 활용)
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
result = [[a[i][j] + b[i][j] for j in range(m)] for i in range(n)]
for row in result:
    print(*row)
```

### 2. 딕셔너리를 활용한 데이터 매핑

#### 문제: 25206 (너의 평점은)
- **핵심 문법**: 딕셔너리, 가중 평균 계산, 조건부 처리
- **학습 포인트**:
  - 딕셔너리로 학점 매핑
  - 가중 평균 계산: (학점 × 학점수)의 합 / 학점수의 합
  - 'P' 학점 제외 처리

**개선된 코드 예시**:
```python
# 25206번 - 더 간결한 버전
grade_dict = {
    'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0
}

total_score = 0.0
total_credit = 0.0

for _ in range(20):
    _, credit, grade = input().split()
    if grade == 'P':
        continue
    credit = float(credit)
    total_score += credit * grade_dict[grade]
    total_credit += credit

print(total_score / total_credit)
```

### 3. 문자열 패턴 검사 (그룹 단어 체커)

#### 문제: 1316 (그룹 단어 체커)
- **핵심 문법**: 리스트 인덱싱, `ord()`, 불리언 플래그, 문자열 순회
- **학습 포인트**:
  - 그룹 단어: 각 문자가 연속해서 나타나는 단어
  - 이전에 나온 문자를 추적하여 그룹 단어 여부 판단
  - 불리언 배열로 문자 출현 여부 체크

**개선된 코드 예시**:
```python
# 1316번 - 더 간결한 버전
n = int(input())
count = 0

for _ in range(n):
    word = input()
    seen = set()
    is_group = True
    prev_char = ''
    
    for char in word:
        if char != prev_char:
            if char in seen:
                is_group = False
                break
            seen.add(char)
        prev_char = char
    
    if is_group:
        count += 1

print(count)

# 또는 더 Pythonic한 버전
n = int(input())
count = 0

for _ in range(n):
    word = input()
    groups = []
    prev = ''
    
    for char in word:
        if char != prev:
            groups.append(char)
            prev = char
    
    if len(groups) == len(set(groups)):  # 중복이 없으면 그룹 단어
        count += 1

print(count)
```

## 🎯 핵심 파이썬 문법 정리

### 1. 2차원 배열(행렬)
- **생성**: `[[0] * m for _ in range(n)]` - n×m 행렬
- **접근**: `matrix[i][j]` - i행 j열 요소
- **순회**: 중첩 반복문으로 행과 열 순회
- **리스트 컴프리헨션**: `[[expr for j in range(m)] for i in range(n)]`

### 2. 딕셔너리 활용
- **생성**: `{key: value}` 또는 `dict()`
- **접근**: `dict[key]` 또는 `dict.get(key, default)`
- **키 존재 확인**: `key in dict`
- **순회**: `for key, value in dict.items()`

### 3. 문자열 패턴 검사
- **문자 출현 추적**: 리스트 또는 집합 활용
- **연속 문자 체크**: 이전 문자와 비교
- **그룹 단어 판단**: 각 문자가 연속해서만 나타나는지 확인

### 4. 가중 평균 계산
- **공식**: (값 × 가중치)의 합 / 가중치의 합
- **구현**: 누적 변수 두 개 사용 (분자, 분모)

## 💡 효율성 개선 팁

1. **2차원 배열 생성**:
   - 리스트 컴프리헨션으로 간결하게 생성
   - `[[0] * m] * n`은 얕은 복사 문제가 있으므로 주의

2. **최댓값/최솟값 찾기**:
   - `enumerate()`로 인덱스와 값 동시 접근
   - 초기값 설정 주의 (음수 가능성 고려)

3. **딕셔너리 활용**:
   - 매핑이 필요한 경우 딕셔너리 사용
   - `dict.get(key, default)`로 안전하게 접근

4. **그룹 단어 체크**:
   - `set`을 활용하여 중복 확인 간소화
   - 이전 문자와 비교하여 연속성 체크

5. **가중 평균**:
   - 분자와 분모를 별도로 누적
   - 0으로 나누는 경우 주의

## 🔍 문제별 핵심 포인트

### 10798번 (세로로 읽기)
- **핵심**: 행과 열의 인덱스를 바꿔서 접근
- **주의**: 각 단어의 길이가 다를 수 있음

### 2566번 (최댓값)
- **핵심**: 2차원 배열에서 최댓값과 그 위치 찾기
- **주의**: 인덱스는 1부터 시작 (문제 조건)

### 2738번 (행렬 덧셈)
- **핵심**: 같은 크기의 행렬을 요소별로 더하기
- **주의**: 행과 열의 크기 일치 확인

### 25206번 (너의 평점은)
- **핵심**: 가중 평균 계산
- **주의**: 'P' 학점은 계산에서 제외

### 1316번 (그룹 단어 체커)
- **핵심**: 문자가 연속해서만 나타나는지 확인
- **주의**: 같은 문자가 떨어져서 나타나면 그룹 단어 아님

